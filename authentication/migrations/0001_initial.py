# Generated by Django 4.0.5 on 2022-06-06 04:39

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether this user has completed the email verification process to allow login.', verbose_name='verified')),
                ('AccountType', models.CharField(choices=[('Leesee', 'Leesee'), ('Leeser', 'Leesser')], max_length=256)),
                ('cool_name', models.CharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator], verbose_name='Username')),
                ('Gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=255)),
                ('Phone_number', models.CharField(max_length=255)),
                ('is_completely_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelLeesee',
            fields=[
                ('Leesee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Business_name', models.CharField(max_length=150)),
                ('business_address', models.CharField(max_length=150)),
                ('CAC', models.CharField(max_length=150)),
                ('VerificationMethod', models.CharField(choices=[('BVN', 'BVN'), ('NIN', 'NIN')], max_length=256)),
                ('VerificationField', models.BigIntegerField()),
            ],
        ),
    ]
