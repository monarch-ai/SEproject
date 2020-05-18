# Generated by Django 3.0.5 on 2020-04-20 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='login.User', verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Category', verbose_name='分类')),
                ('like_users', models.ManyToManyField(related_name='like_users', to='login.User', verbose_name='用户')),
                ('tags', models.ManyToManyField(to='bbs.Tag', verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User', verbose_name='评论者')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Post', verbose_name='帖子')),
            ],
        ),
    ]
