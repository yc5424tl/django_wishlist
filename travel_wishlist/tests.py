from django.test import TestCase
from django.urls import reverse
from .models import Place


class TestViewHomePageIsEmptyList(TestCase):

    def test_load_page_shows_empty_list(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])


class TestWishList(TestCase):

    fixtures = ['test_places']

    def test_view_wishlist(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        data_rendered = list(response.context['places'])
        data_expected = list(Place.objects.filter(visited=False))
        self.assertCountEqual(data_rendered, data_expected)

    def test_view_places_visited(self):

        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        data_rendered = list(response.context['visited'])
        data_expected = list(Place.objects.filter(visited=True))
        self.assertCountEqual(data_rendered, data_expected)


# noinspection PyUnusedLocal
class TestAddNewPlace(TestCase):

    def test_add_new_unvisted_place_to_wishlist(self):

        response = self.client.post(reverse('place_list'), {'name': 'Tokyo', 'visited': False}, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(len(response_places), 1)

        tokyo_response = response_places[0]
        tokyo_in_database = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_response, tokyo_in_database)

        response = self.client.post(reverse('place_list'), {'name': 'Yosemite', 'visited': False}, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(len(response_places), 2)

        place_in_database = Place.objects.get(name='Yosemite', visited=False)
        place_in_database = Place.objects.get(name='Tokyo', visited=False)
        places_in_database = Place.objects.all()
        self.assertCountEqual(list(places_in_database), list(response_places))

    def test_add_new_place_to_wishlist(self):

        response = self.client.post(reverse('place_list'), {'name': 'Tokyo', 'visited': True}, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(len(response_places), 0)

        place_in_database = Place.objects.get(name='Tokyo', visited=True)


