# Generated by Django 3.2.20 on 2023-08-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=50)),
                ('video_id', models.CharField(max_length=50)),
                ('comment_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('video_id', models.CharField(max_length=50)),
                ('reaction', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('channel_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('thumbnail', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VideoTag',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('video_id', models.CharField(max_length=50)),
                ('tag_id', models.CharField(max_length=50)),
            ],
        ),
    ]
