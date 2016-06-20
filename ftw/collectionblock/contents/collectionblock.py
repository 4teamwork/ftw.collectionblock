from ftw.collectionblock import _
from ftw.collectionblock.contents.interfaces import ICollectionBlock
from plone.app.contenttypes.content import Collection
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implements


class ICollectionBlockSchema(model.Schema):
    """Collection block for simplelayout
    """

    title = schema.TextLine(
        title=_(u'collectionblock_title_label', default=u'Title'),
        required=True,
    )

    directives.order_before(title='*')

    show_title = schema.Bool(
        title=_(u'collectionblock_show_title_label', default=u'Show title'),
        default=False,
        required=False,
    )

    directives.order_after(show_title='title')

alsoProvides(ICollectionBlockSchema, IFormFieldProvider)


class CollectionBlock(Collection):
    implements(ICollectionBlock)
