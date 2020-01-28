# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-27 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

try:
    from wagtail.contrib.routable_page.models import RoutablePageMixin
    from wagtail.core import blocks
    from wagtail.core import fields
except ImportError:
    from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailcore import fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailregulations', '__first__'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRegulationLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', fields.StreamField((('title', blocks.CharBlock()), ('introduction', blocks.RichTextBlock()), ('regulations_list', blocks.StructBlock((('heading', blocks.CharBlock(help_text='Regulations list heading', required=False)), ('more_regs_page', blocks.PageChooserBlock(help_text='Link to more regulations')), ('more_regs_text', blocks.CharBlock(help_text='Text to show on link to more regulations', required=False)))))))),
            ],
            options={
                'abstract': False,
            },
            bases=(RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='TestRegulationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', fields.StreamField((('title', blocks.CharBlock()), ('introduction', blocks.RichTextBlock())))),
                ('regulation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='page', to='wagtailregulations.Part')),
            ],
            options={
                'abstract': False,
            },
            bases=(RoutablePageMixin, 'wagtailcore.page', models.Model),
        ),
    ]
