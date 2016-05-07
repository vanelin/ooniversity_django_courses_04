# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client

from students.models import Student
from courses.models import Course


class StudentsListTest(TestCase):

    def test_index_1(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_index_2(self):
        response = self.client.get('/students/')
        self.assertTrue('student_list' in response.context)

    def test_view_title(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'PyBursa students list')

    def test_Entry_Fields_Links(self):
        course = Course.objects.create(
            name='Django Base',
            short_description='Django Base Course')
        course.save()
        student = Student(
            name="Ivan",
            surname="Ivanov",
            date_of_birth="1999-09-09",
            email="test@test.com",
            phone="1234567890",
            address="Mykolyiv",
            skype="test")
        student.save()
        student.courses.add(course)
        response = self.client.get('/students/')
        self.assertContains(response, 'Django Base')
        self.assertContains(response, '/students/edit/{}/'.format(student.id))
        self.assertContains(response, '/students/remove/{}/'.format(student.id))
        self.assertContains(response, '/students/add/')
        self.assertEqual(student.name, "Ivan")
        self.assertEqual(student.date_of_birth, "1999-09-09")
        self.assertEqual(course.name, 'Django Base')
        self.assertEqual(student.courses.all()[0], course)

    def test_pagination(self):
        for name in ["test1", "test2", "test3", "test4"]:
            Student.objects.create(
                name=name,
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
        response = self.client.get('/students/')
        self.assertContains(response, 'next >>')

    def test_student_remove(self):
            student = Student.objects.create(
                name='Ivan',
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
            self.assertEqual(Student.objects.all().count(), 1)
            student.delete()
            self.assertEqual(Student.objects.all().count(), 0)


class StudentsDetailTest(TestCase):

    def test_index(self):
        student = Student.objects.create(
                name='Ivan',
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_Template_Title(self):
        student = Student.objects.create(
                name='Ivan',
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
        response = self.client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')
        self.assertContains(response, 'Student detail - PyBursa')

    def test_detail_item(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student = Student.objects.create(
                name='Ivan',
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_link_course(self):
        course = Course.objects.create(
            name='Django Base',
            short_description='Django Base Course')
        course.save()
        student = Student(
            name="Ivan",
            surname="Ivanov",
            date_of_birth="1999-09-09",
            email="test@test.com",
            phone="1234567890",
            address="Mykolyiv",
            skype="test")
        student.save()
        student.courses.add(course)
        response = self.client.get('/students/1/')
        self.assertContains(response, '/courses/{}/'.format(student.id))
        self.assertContains(response, 'Django Base')

    def test_detail(self):
        student = Student.objects.create(
                name='Ivan',
                surname="Ivanov",
                date_of_birth="1999-09-09",
                email="test@test.com",
                phone="1234567890",
                address="Mykolyiv",
                skype="test")
        response = self.client.get('/students/1/')
        self.assertEqual(response.context['student'].pk, 1)
        self.assertEqual(response.context['student'].email, 'test@test.com')

        # Ensure that non-existent polls throw a 404.
        response = self.client.get('/students/2/')
        self.assertEqual(response.status_code, 404)
