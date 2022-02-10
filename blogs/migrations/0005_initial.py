# Generated by Django 4.0.2 on 2022-02-08 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0004_remove_answer_res_by_delete_answerimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('answer', models.TextField()),
                ('res_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='answer_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('species_name', models.CharField(max_length=255)),
                ('species_detail', models.TextField()),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='question_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('question', models.TextField()),
                ('number_of_likes', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.answer')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.questionimage')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
