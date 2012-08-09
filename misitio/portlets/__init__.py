from zope.i18nmessageid import MessageFactory
MyDemoPortletMessageFactory = MessageFactory('misitio.portlets')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
