from django.test import TestCase
from .models import React, User, CollectionPoint, WasteBin, CollectionRoute, WasteCollectionRecord, WasteDisposalSite, DisposalRecord, Report
from django.contrib.auth.models import User as AuthUser

class ModelTestCase(TestCase):

    def setUp(self):
        self.user_role = 'Admin'
        self.user = User.objects.create(
            name='John Doe',
            role=self.user_role,
            contact_number='1234567890',
            address='123 Main St, City',
        )

        self.collection_point = CollectionPoint.objects.create(
            name='Point A',
            location='Coordinates',
            description='A collection point',
            collection_schedule='Every day',
            capacity=100,
            supervisor=self.user
        )

        self.waste_bin = WasteBin.objects.create(
            point=self.collection_point,
            capacity=50,
            current_fill_level=30,
            last_emptied_date='2023-08-12 10:00:00',
            status='Operational',
            type='General'
        )

        # Similarly, create instances of other models for testing

    def test_user_model(self):
        user = User.objects.get(name='John Doe')
        self.assertEqual(user.role, self.user_role)

    def test_collection_point_model(self):
        collection_point = CollectionPoint.objects.get(name='Point A')
        self.assertEqual(collection_point.capacity, 100)

    def test_waste_bin_model(self):
        waste_bin = WasteBin.objects.get(point__name='Point A')
        self.assertEqual(waste_bin.capacity, 50)

    # Add more test methods for other models
