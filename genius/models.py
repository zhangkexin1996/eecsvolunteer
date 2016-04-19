# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CaseHistoryStatus:
    def __init__(self):
        pass
    unknown = 0
    waiting_for_repair = 1
    repairing = 2
    repaired = 3

    choices = (
        (unknown, u'未知'),
        (waiting_for_repair, u'待维修'),
        (repairing, u'正在维修'),
        (repaired, u'已维修')
    )


class Activity(models.Model):
    date = models.IntegerField(u'活动日期')
    place = models.CharField(u'活动地点', max_length=45, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.date)

    class Meta:
        db_table = 'activity'


class CaseHistory(models.Model):
    activity = models.ForeignKey(Activity)
    computer_model = models.CharField(u'电脑型号', max_length=128)
    problem = models.TextField(u'问题描述', max_length=512)
    solution = models.TextField(u'解决办法', max_length=1024)
    status = models.IntegerField(u'病例单状态', choices=CaseHistoryStatus.choices, default=CaseHistoryStatus.unknown)
    volunteer = models.TextField(u'志愿者', max_length=512)

    def __unicode__(self):
        return u'{0}'.format(self.id)

    class Meta:
        db_table = 'case_history'


