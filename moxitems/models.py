from django.db import models

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
        upload_to = 'podcast_images'
    )
    
    email = models.EmailField(
        help_text = "An e-mail address which people with queries about the feed content can contact"
    )
    
    language = models.CharField(
        help_text = "The <a href='http://www.rssboard.org/rss-language-codes'>ISO 639 language code</a> of the language this feed is published in",
        default = "en-gb",
        max_length = 8
    )
    
    include_in_podcasts = models.BooleanField(
        help_text = "Whether or not this feed should be included in podcasts.ox.ac.uk"
    )
    
    include_in_itunesu = models.BooleanField(
        help_text = "Whether or not this feed should be included in iTunes U"
    )
    
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
    
    # TODO
    #
    # Do we need...
    # * short_name
    # * GUID
    #
    # Many-to-many needed for:
    # * Template
    # * Relevant OxPoints units
    # * Licence
    #
    # Need to add Django custom functionality for:
    # * Modified by, etc (auditing)
    # * Visibility
    # * Tagging
    # * permissions