# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

from courses.models import Course, Lesson
from coaches.models import Coach


class CoursesListTest(TestCase):

    """docstring for CoursesListTest"""

    def test_list_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'PyBursa Description')

    def test_course_create(self):
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        response = self.client.get('/')
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_link_remove_edit_course(self):
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        response = self.client.get('/')
        self.assertContains(response, '/courses/edit/{}/'.format(course.id))
        self.assertContains(response, '/courses/remove/{}/'.format(course.id))

    def test_remove_course(self):
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        self.assertEqual(Course.objects.all().count(), 1)
        course.delete()
        self.assertEqual(Course.objects.all().count(), 0)


class CoursesDetailTest(TestCase):

    """docstring for CoursesDetailTest"""

    def test_url(self):
        client = Client()
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_detail_item(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course = Course.objects.create(
            name='PyBursa test course',
            short_description='Web development with django')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_model_relation(self):
        course = Course.objects.create(name='test1')
        lesson = Lesson(course=Course.objects.create(name='test2'),
                        subject='test1',
                        description='test1',
                        order=int('1')
                        )
        lesson.full_clean()  # `course` correctly set. This should pass
        lesson.save()
        self.assertEqual(
            Lesson.objects.filter(course__name='test2').count(), 1)

    def test_model_relation_course_missing(self):
        course = Course.objects.create(name='test1')
        lesson = Lesson()  # Lesson without `course` set
        with self.assertRaises(ValidationError):
            lesson.full_clean()
            lesson.save()
        self.assertEqual(
            Lesson.objects.filter(course__name='test2').count(), 0)

    def test_coach(self):
        client = Client()
        coach = Coach.objects.create(
            user=User.objects.create_user(
                username='coach_1',
                password='qwerty',
                first_name=u'Ivan',
                last_name=u'Ivanov',
                email='coach_1@coach.com'),
            date_of_birth='1988-01-01',
            gender='M',
            phone='1234657980',
            address='Mykolayiv',
            skype='ivan',
            description='admin',)
        course = Course.objects.create(name='PyBursa test course',
                                       short_description='Web development with django',
                                       coach=Coach.objects.get(id=1)
                                       )
        response = client.get('/courses/1/')
        self.assertContains(response, 'Ivan Ivanov')
        self.assertEqual(response.status_code, 200)
