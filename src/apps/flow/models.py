import json

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_fsm import FSMField, transition

from src.constants import CREATED, DELIVER, DISPATCH, PICK, READY_TO_DISPATCH, RECEIVE, SHELVE
from .utils import TRANSITIONS, transition_filename


class Order(models.Model):
    """
    Workflow for OrderFlow
    """

    state = FSMField(default=CREATED, protected=True)
    awb = models.CharField(max_length=20, unique=True, null=False, blank=False)

    @transition(field=state, source=TRANSITIONS.get(PICK), target=PICK,
                custom=dict(verbose='order is Picked from the Client'))
    def pick(self):
        """
        Pick Orders
        :param by:
        :return:
        """
        return {'success': True, 'message': 'Picked successfully'}

    @transition(field=state, source=TRANSITIONS.get(RECEIVE), target=RECEIVE,
                custom=dict(verbose='order is received from the Client'))
    def receive(self):
        """
        Receive Orders
        :return:
        """
        return {'success': True, 'message': 'Received successfully'}

    @transition(field=state, source=TRANSITIONS.get(SHELVE), target=SHELVE,
                custom=dict(verbose='Order is shelved in our warehouse'))
    def shelve(self):
        """
        Shelve Orders
        :return:
        """
        return {'success': True, 'message': 'Shelved successfully'}

    @transition(field=state, source=TRANSITIONS.get(READY_TO_DISPATCH), target=READY_TO_DISPATCH, on_error=SHELVE)
    def ready_to_dispatch(self):
        """
        Ready to dispatch orders
        :return:
        """
        return {'success': True, 'message': 'Ready to dispatch successful'}

    @transition(field=state, source=TRANSITIONS.get(DISPATCH), target=DISPATCH,
                on_error=READY_TO_DISPATCH)
    def dispatch(self):
        """
        Dispatch Orders
        :return:
        """
        return {'success': True, 'message': 'Dispatched successfully'}

    @transition(field=state, source=TRANSITIONS.get(DELIVER), target=DELIVER,
                on_error=DISPATCH)
    def deliver(self):
        """
        Deliver Orders
        :return:
        """
        return {'success': True, 'message': 'delivered successfully'}

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class State(models.Model):
    """
    States name and codes
    """

    name = models.CharField(max_length=130, verbose_name='State Name')
    code = models.CharField(max_length=10, verbose_name='State Code', unique=True)

    class Meta:
        verbose_name_plural = 'States'

    def __str__(self):
        return "{} ({})".format(self.name, self.code)


class StateTransition(models.Model):
    """
    Holds transitions for Orders
    """

    source = models.ForeignKey(State, related_name='state_flow_source', on_delete=models.CASCADE)
    target = models.ForeignKey(State, related_name='state_flow_target', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('source', 'target')

    def __str__(self):
        return "{} -- {}".format(self.source, self.target)


@receiver(post_save, sender=StateTransition)
def update_and_create_transitions_json(sender, instance, **kwargs):
    """
    Creates a json file for transitions
    """
    transitions = {}
    for target, source in StateTransition.objects.values_list('target__code', 'source__code'):
        if target in transitions:
            transitions[target].append(source)
        else:
            transitions[target] = [source]

    with open(transition_filename, 'w+') as file:
        file.write(json.dumps(transitions))
