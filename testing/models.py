from django.db import models

POST, GET = "post", 'get'


class Course(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.name}'


class Testes(models.Model):
	name = models.CharField(max_length=50)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} {self.course.name}"


class UnitTestes(models.Model):
	METHOD_CHOICE = (
		(POST, POST),
		(GET, GET),
	)
	test = models.ForeignKey(Testes, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255, null=True, blank=True)
	url = models.CharField(max_length=150)
	method = models.CharField(max_length=20, choices=METHOD_CHOICE)
	param = models.JSONField(null=True, blank=True)
	json = models.JSONField(null=True,  blank=True)
	status_code = models.IntegerField(default=0, null=True, blank=True)
	is_list = models.BooleanField(default=False)
	is_contains = models.CharField(max_length=100, null=True, blank=True)
	key = models.JSONField(null=True, blank=True)


	def __str__(self):
		return f"{self.name} {self.test.name}"



