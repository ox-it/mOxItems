from django.db import models

#TODO figure out which of these are not required by default

class Licence(models.Model):
    """
    A model which represents possible licences
    """
    name = models.CharField(
        help_text = "Name of licence",
        max_length= 128
    )
    url = models.URLField(
        help_text = "URL to licence text"
    )
    # TODO logo field maybe needed here - link to local image?
    
    def __unicode__ (self):
        return self.name

class Template(models.Model):
    """
    A model which defines smarty templates to transform data
    """
    name = models.CharField(
        help_text = "Name of template",
        max_length = 200
    )
    description = models.TextField(
        help_text = "Explanation of what this template achieves"
    )
    #TODO Check the following two fields for accuracy.
    template = models.TextField(
        help_text = "Contents of template (for internal storage)"
    )
    url = models.URLField(
        help_text = "URL to external template - ideally should not be used."
    )
    
    def __unicode__ (self):
        return self.name

class Feed(models.Model):
    """
    A model which represents a feed
    """
    
    slug = models.SlugField(
        help_text = "The name in the form 'unit/feed' which is used to refer to the feed in URLs, e.g., oucs/events",
        unique = True
    )
    
    title = models.CharField(
        help_text = "The human readable name of this feed, e.g., Oxford University Computing Services Events",
        max_length = 200
    )
    
    link = models.URLField(
        help_text = "A link to a page which contains information about this feed"
    )
    
    description = models.TextField(
        help_text = "A human readable description of what this feed is about"
    )
    
    image = models.ImageField(
        help_text = "An image (or icon) which represents this podcast feed",
        upload_to = 'feed_images',
        blank = True
    )
    
    email = models.EmailField(
        help_text = "An e-mail address which people with queries about the feed content can contact"
    )
    
    language = models.CharField(
        help_text = "The <a href='http://www.rssboard.org/rss-language-codes'>ISO 639 language code</a> of the language this feed is published in",
        default = "en-gb",
        max_length = 8
    )
    
    guid = models.URLField(
        help_text = "A unique identifier required by the Atom spec (entry - id) and RSS2 (item - guid)",
        verify_exists = False
    )
    
    include_in_podcasts = models.BooleanField(
        help_text = "Whether or not this feed should be included in podcasts.ox.ac.uk"
    )
    
    include_in_itunesu = models.BooleanField(
        help_text = "Whether or not this feed should be included in iTunes U"
    )
    
    # One to many relationships
    licence = models.ForeignKey(Licence)
    template = models.ForeignKey(Template, null=True, blank=True)
    
    JORUMOPEN_COLLECTIONS = (
        ('', 'None'),
        ('FE', (
                ('FE - Agriculture Horticulture & Animal Care', 'Agriculture Horticulture & Animal Care'),
                ('FE - Area Studies / Cultural Studies / Languages / Literature', 'Area Studies / Cultural Studies / Languages / Literature'),
                ('FE - Arts & Crafts', 'Arts & Crafts'),
                ('FE - Business / Management / Office Studies', 'Business / Management / Office Studies'),
                ('FE - Catering / Food / Leisure Services / Tourism', 'Catering / Food / Leisure Services / Tourism'),
                ('FE - Communication / Media / Publishing', 'Communication / Media / Publishing'),
                ('FE - Construction & Property (Built Environment)', 'Construction & Property (Built Environment)'),
                ('FE - Education / Training / Teaching', 'Education / Training / Teaching'),
                ('FE - Engineering', 'Engineering'),
                ('FE - Environment Protection / Energy / Cleansing / Security', 'Environment Protection / Energy / Cleansing / Security'),
                ('FE - Family Care / Personal Development / Personal Care & Appearance', 'Family Care / Personal Development / Personal Care & Appearance'),
                ('FE - Health Care / Medicine / Health & Safety', 'Health Care / Medicine / Health & Safety'),
                ('FE - Humanities (History / Archaeology / Religious Studies / Philosophy)', 'Humanities (History / Archaeology / Religious Studies / Philosophy)'),
                ('FE - Information Technology & Information', 'Information Technology & Information'),
                ('FE - Logistics / Distribution / Transport / Driving', 'Logistics / Distribution / Transport / Driving'),
                ('FE - Manufacturing / Production Work', 'Manufacturing / Production Work'),
                ('FE - Oil / Mining / Plastics / Chemicals', 'Oil / Mining / Plastics / Chemicals'),
                ('FE - Performing Arts', 'Performing Arts'),
                ('FE - Politics / Economics / Law / Social Sciences', 'Politics / Economics / Law / Social Sciences'),
                ('FE - Sales Marketing & Retailing', 'Sales Marketing & Retailing'),
                ('FE - Sciences & Mathematics', 'Sciences & Mathematics'),
                ('FE - Services to Industry & Commerce', 'Services to Industry & Commerce'),
                ('FE - Sports Games & Recreation', 'Sports Games & Recreation')
            )
        ),
        ('HE', (
                ('HE - Architecture, Building and Planning', 'Architecture, Building and Planning'),
                ('HE - Biological Sciences', 'Biological Sciences'),
                ('HE - Business and Administrative studies', 'Business and Administrative studies'),
                ('HE - Creative Arts and Design', 'Creative Arts and Design'),
                ('HE - Eastern, Asiatic, African, American and Australasian Languages, Literature and related subjects', 'Eastern, Asiatic, African, American and Australasian Languages, Literature and related subjects'),
                ('HE - Education', 'Education'),
                ('HE - Engineering', 'Engineering'),
                ('HE - European Languages, Literature and related subjects', 'European Languages, Literature and related subjects'),
                ('HE - Historical and Philosophical studies', 'Historical and Philosophical studies'),
                ('HE - Law', 'Law'),
                ('HE - Linguistics, Classics and related subjects', 'Linguistics, Classics and related subjects'),
                ('HE - Mass Communications and Documentation', 'Mass Communications and Documentation'),
                ('HE - Mathematical and Computer Sciences', 'Mathematical and Computer Sciences'),
                ('HE - Medicine and Dentistry', 'Medicine and Dentistry'),
                ('HE - Physical Sciences', 'Physical Sciences'),
                ('HE - Social studies', 'Social studies'),
                ('HE - Subjects allied to Medicine', 'Subjects allied to Medicine'),
                ('HE - Technologies', 'Technologies'),
                ('HE - Veterinary Sciences, Agriculture and related subjects', 'Veterinary Sciences, Agriculture and related subjects'),
            )
        )
    )
    
    jorumopen_collection = models.CharField(
        help_text = 'The name of the JorumOpen collection this feed belongs to',
        choices = JORUMOPEN_COLLECTIONS,
        default = '',
        max_length = 100
    )
    
    SORT_ORDERS = (
        ('A', 'Ascending'),
        ('D', 'Descending')
    )
    
    sort_order = models.CharField(
        help_text = "How items in this feed should be ordered",
        choices = SORT_ORDERS,
        default = 'D',
        max_length = 1
    )
    
    SORT_FIELDS = (
        ('author', 'Alphabetically by author name'),
        ('content', 'Alphabetically by content'),
        ('id', 'Numerically by ID'),
        ('published', 'Chronologically by publish date'),
        ('summary', 'Alphabetically by summary'),
        ('title', 'Alphabetically by title'),
        ('updated', 'Chronologically by updated date')
    )
    
    sort_by = models.CharField(
        help_text = "Which field is used to determine how items are ordered",
        choices = SORT_FIELDS,
        default = 'published',
        max_length = 10
    )
    
    def __unicode__ (self):
        return self.title

class Item(models.Model):
    feed = models.ForeignKey(Feed)
    
    title = models.CharField(
        help_text = "The human readable title of this item",
        max_length = 200
    )
    
    #TODO Look at this field in more detail - e.g. what happens when we have a departmental author as well as in individual
    author = models.TextField(
        help_text = "The name of the author(s) of this item"
    )
    
    link = models.URLField(
        help_text = "A link to the original article. If this is left blank, we will generate a news page for you or link to the podcast url."
    )
    
    content = models.TextField(
        help_text = "The content of this item"
    )
    
    summary = models.TextField(
        help_text = "A summary of the item content e.g. brief description. If you leave this blank we will take the first X words from content."
    )
    
    expires = models.DateTimeField(
        help_text = "The date and time this item will be removed from the feed (but still visible here)."
    )
    
    guid = models.URLField(
        help_text = "A unique identifier required by the Atom spec (entry - id) and RSS2 (item - guid)",
        verify_exists = False
    )
    
    published = models.DateTimeField(
        help_text = "The date and time at which this item was published (if set to a time in the future it will remain hidden until that time)"
    )
    
    podcast_link = models.URLField(
        help_text = "Link to the relevant podcast media file e.g. http://example.com/podcast.mp3"
    )
    
    podcast_author = models.TextField(
        help_text = "Authors/Presenters who made this podcast"
    )
    # TODO podcast_type and podcast_length should be generated by checking file type.
    
    podcast_recording_date = models.DateTimeField(
        help_text = "The date this podcast was recorded"
    )
    
    licence = models.ForeignKey(Licence)
    
    def __unicode__ (self):
        return self.title
    # TODO podcast duration maybe needed but ideally derived.

    
    
    
    
    
    

    
    
    # TODO
    #
    # Do we need...
    # * short_name
    # * GUID
    #
    # Many-to-many needed for:
    # * Relevant OxPoints units
    #
    # Need to add Django custom functionality for:
    # * Modified by, etc (auditing)
    # * Visibility
    # * Tagging
    # * permissions
