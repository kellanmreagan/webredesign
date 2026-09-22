#!/usr/bin/env python3
"""Generate the static Rugged Country Lodge redesign pages."""

from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent
BOOK = "https://book.bookingcenter.com/03/?site=RUGGED"
PHONE = "(541) 966-6800"
PHONE_TEL = "tel:5419666800"
EMAIL = "info@ruggedcountrylodge.com"
ADDR = "1807 SE Court Avenue, Pendleton, OR 97801, United States"
FACEBOOK = "https://facebook.com/RuggedCountryLodge/"
GOOGLE_REVIEWS = "https://www.google.com/travel/search?q=rugged%20country%20lodge"
TRIPADVISOR = "https://tripadvisor.com/Hotel_Review-g52016-d579587-Reviews-Rugged_Country_Lodge-Pendleton_Oregon.html"
MAP = "https://www.google.com/maps/d/embed?mid=1N_Cc5QAvkjF0P4c7t5sWUSH8edE"

NAV = [
    ("book", "Book Now", BOOK, None),
    ("home", "Home", "index.html", None),
    (
        "rooms",
        "Rooms",
        "rooms.html",
        [
            ("rooms-single", "Single Room", "rooms/single-room.html"),
            ("rooms-double", "Double Room", "rooms/double-room.html"),
            ("rooms-mini", "Mini Suite", "rooms/mini-suite.html"),
            ("rooms-standard", "Standard Suite", "rooms/standard-suite.html"),
        ],
    ),
    (
        "about",
        "About Us",
        "about-us.html",
        [
            ("about-history", "Our History", "about-us.html"),
            ("about-story", "Our Story", "about-us/our-story.html"),
            ("about-amenities", "Amenities", "about-us/amenities.html"),
            ("about-mission", "Mission Statement", "about-us/mission-statement.html"),
        ],
    ),
    ("location", "Location", "location.html", None),
    ("gallery", "Photo Gallery", "photo-gallery.html", None),
    ("policies", "Policies", "policies.html", None),
    ("contact", "Contact", "contact.html", None),
]


def rel(path, depth):
    return ("../" * depth) + path


def e(text):
    return html.escape(text, quote=True)


def img(prefix, src, alt, extra=""):
    return f'<img src="{prefix}images/{src}" alt="{e(alt)}"{(" " + extra) if extra else ""}>'


def header(page, depth):
    p = rel("", depth)
    nav_html = ["<ul>"]
    for key, label, href, children in NAV:
        active = page == key or (children and any(page == c[0] for c in children))
        cls = "has-sub" if children else ""
        if active:
            cls = (cls + " is-active").strip()
        current = ' aria-current="page"' if page == key else ""
        nav_html.append(f'<li class="{cls}">')
        if href.startswith("http"):
            nav_html.append(f'<a href="{href}" target="_blank" rel="noopener">{e(label)}</a>')
        else:
            nav_html.append(f'<a href="{rel(href, depth)}"{current}>{e(label)}</a>')
        if children:
            nav_html.append('<ul class="sub">')
            for ckey, clabel, chref in children:
                cur = ' aria-current="page"' if page == ckey else ""
                nav_html.append(f'<li><a href="{rel(chref, depth)}"{cur}>{e(clabel)}</a></li>')
            nav_html.append("</ul>")
        nav_html.append("</li>")
    nav_html.append("</ul>")
    return f"""
<header class="site-header">
  <div class="wrap header-bar">
    <a class="brand" href="{rel("index.html", depth)}">
      {img(p, "xntayzakcqjeqvi3vcg1-1.png", "Rugged Country Lodge")}
      <span class="brand-text"><strong>Rugged Country Lodge</strong><span>Pendleton, Oregon</span></span>
    </a>
    <div class="header-actions">
      <a class="header-phone" href="{PHONE_TEL}">{PHONE}</a>
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">BOOK NOW</a>
      <a class="nav-toggle" href="#site-nav" aria-expanded="false" aria-controls="site-nav">Menu</a>
    </div>
  </div>
  <nav class="site-nav" id="site-nav" aria-label="Primary">{"".join(nav_html)}</nav>
</header>
"""


def footer(depth, page=None):
    p = rel("", depth)
    terms_attr = ' class="is-active" aria-current="page"' if page == "terms" else ""
    a11y_attr = ' class="is-active" aria-current="page"' if page == "a11y" else ""
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Rugged Country Lodge</h2>
      <p>{e(ADDR)}<br>
      P: <a href="{PHONE_TEL}">{PHONE}</a><br>
      E: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h2>Stay</h2>
      <ul>
        <li><a href="{rel("rooms.html", depth)}">Rooms</a></li>
        <li><a href="{rel("photo-gallery.html", depth)}">Photo Gallery</a></li>
        <li><a href="{rel("policies.html", depth)}">Policies</a></li>
        <li><a href="{BOOK}" target="_blank" rel="noopener">Book Now</a></li>
      </ul>
    </div>
    <div>
      <h2>Visit</h2>
      <ul>
        <li><a href="{rel("about-us.html", depth)}">About Us</a></li>
        <li><a href="{rel("location.html", depth)}">Location</a></li>
        <li><a href="{rel("contact.html", depth)}">Contact</a></li>
        <li><a href="{rel("about-us/amenities.html", depth)}">Amenities</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>© 2026 Rugged Country Lodge</span>
    <nav>
      <a href="{rel("terms-privacy.html", depth)}"{terms_attr}>Privacy Statement</a>
      <a href="{rel("accessibility-statement.html", depth)}"{a11y_attr}>Accessibility Statement</a>
    </nav>
  </div>
</footer>
<script src="{p}js/site.js?v=2"></script>
"""


def page(filename, title, description, nav, depth, body, hero_style=""):
    p = rel("", depth)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <link rel="icon" href="{p}favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}css/site.css?v=2">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
{header(nav, depth)}
<main id="content">
{body}
</main>
{footer(depth, nav)}
</body>
</html>
"""
    path = ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc)
    print("wrote", path.relative_to(ROOT))


def page_hero(title, kicker="Pendleton, Oregon", lede="", bg="", prefix=""):
    style = f' style="background-image:url({prefix}images/{bg})"' if bg else ""
    extra = f"<p>{lede}</p>" if lede else ""
    return f"""
<section class="page-hero"{style}>
  <div class="wrap">
    <p class="kicker">{e(kicker)}</p>
    <h1>{title}</h1>
    {extra}
  </div>
</section>
"""


ROOM_SHARED = """
<p>You’ll see at a glance that we intend to be your home away from home. No lack luster, boring motel furniture here! We’ve purposely chosen Broyhill’s Attic Heirloom hardwood furnishings in an eclectic mix of colors and styles designed to make you feel right at home. Our choice of quality artwork by Albrecht Bierstadt and Thomas Moran perfectly accent our lodge style and themes of nature so intertwined in this corner of Northeastern Oregon. While keeping with our themes, our 29 room layouts are varied and many foot prints are a little bit different. We’re especially proud of our original vintage tiled bathrooms that boast a mix of colors from room to room.</p>
<p>Our Broyhill armoire holds a 32” crystal-clear {tv} with over 50 cable channels, l though we’re in the process of upgrading to flat screen HD TV. The armoire’s two drawers are ample to hold your personal belongings (after you remove polar fleece blanket). For your convenience, clock-radios, microwaves and refrigerators are found in each room and ice is available during office hours. Twenty-four hour wake up service and voice messaging are included on your phone, so you can dream soft. All rooms offer blackout privacy curtains, large mirrors, door view ports, dead bolts, luggage racks, ice buckets, wrapped cups, bottled water seasonally, closets with hangers, stationery and pens, mints, wireless internet and free local calls. We offer access for the handicapped.</p>
<p>Our quaint vintage-tiled bathrooms are outfitted with thick, luxurious towels, spa quality amenities, a cushy bath mat and a squeaky clean shower and tub unit. The 1950’s period renovated bathroom includes elongated toilet and a pedestal sink with a privacy window.</p>
<p>CANCELLATION POLICY: Guests may cancel reservations up to 24-hours before scheduled arrival without incurring any cancellation penalties. Cancellations made less than 24-hours prior to a guest’s scheduled arrival will be charged for one night’s stay. Thank you for your courtesy!</p>
<p>All of Rugged Country Lodge’s up-scaled boutique rooms are sparkling clean and non-smoking. Guests who smoke in our rooms will be charged up to $250 in cleaning fees.</p>
<p>Rugged Country Lodge welcomes up to two pets. (If you have more than two pets, please call to see if we are able to accommodate your needs and what the fee would be.) We have designated pet-friendly rooms available. However, a non-refundable $15 pet fee (per pet) is required per each night’s stay.. Undisclosed pets will be charged $50.</p>
<p class="note">NEWLY CARPETED THROUGHOUT THE MOTEL</p>
"""


def room_page(photos, prefix):
    first, rest = photos[0], photos[1:]
    thumbs = "".join(
        f'<a href="{prefix}images/{src}" data-lightbox>{img(prefix, src, alt)}</a>'
        for src, alt in rest
    )
    return f"""
<div class="room-gallery">
  <a href="{prefix}images/{first[0]}" data-lightbox>{img(prefix, first[0], first[1])}</a>
  <div class="room-thumbs">{thumbs}</div>
</div>
"""


def build_home():
    p = ""
    glance = [
        ("IMG_0277-scaled.jpg", "A motel with a sign that says lodge on it"),
        ("IMG_0234-scaled.jpg", "A hotel room with two beds and a television."),
        ("IMG_4453-rotated.jpg", "A kitchen with wooden cabinets and shelves filled with various items"),
        ("nrfj3u0q5kbh4nbeithp.png", "A kitchen with a table and chairs in front of two windows"),
        ("IMG_4458.jpg", "A bathroom shelf with a towel , soap and lotion on it."),
        ("IMG_4452-rotated.jpg", "A cereal dispenser sits on a counter in a kitchen"),
        ("IMG_0278-scaled.jpg", "A large building with a green roof is sitting next to a snowy road."),
        ("IMG_4445-rotated.jpg", "A hotel room with a couch and a bed"),
    ]
    glance_html = "".join(
        f'<a href="photo-gallery.html">{img(p, src, alt)}</a>' for src, alt in glance
    )
    body = f"""
<section class="hero" style="background-image:url(images/IMG_0277-scaled.jpg)">
  <div class="wrap hero-inner">
    <p class="kicker">Pendleton, Oregon</p>
    <h1>Welcome to the Rugged Country Lodge!</h1>
    <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book Now</a>
       <a class="btn btn-ghost" href="{PHONE_TEL}">Call {PHONE}</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <p>I’m so happy you discovered Rugged Country Lodge and our website. I’ve got a hunch you found us because you’re someone who’s probably a little bit like me-- you love finding the unexpected lodging, having grown weary of the same old homogenized experience found in all those other chain motels. And I’m betting you want a good value to boot. Well, rest assured, you came to one of the best places to stay in Pendleton!</p>
      <p>As a well- seasoned traveler myself, I’m always looking for that special little place that pays attention to the details, is sparkling clean, feels cozy and warm- -like a bed and breakfast—all the while exuding a unique vintage charm that doesn’t cost an arm and a leg.</p>
      <p>And that’s the fun of Rugged Country! As an independent small business owner I get to do it my way, which means I’ve packaged up all those qualities into one darn cute little place that is anything but boring! Rugged Country Lodge isn’t for everybody, but it is perfect for YOU--the guest who wants a serendipitous vintage experience in an authentic roadside motel in historic Pendleton, Oregon. Once you’re here, we guarantee you’ll dream soft!</p>
    </div>
    <figure class="frame">{img(p, "ekmebcxfsubryajqpclw.jpeg", "A sign for rugged country lodge dream soft")}</figure>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap split">
    <div class="prose">
      <h2>Our Story</h2>
      <h3>Once Upon a Time</h3>
      <p>When I was a little girl I loved playing house. I spent hours fluffing pillows, picking and arranging straggly flower bouquets and constantly reorganizing my parents’ well-worn furniture. Well, I’m all grown up now, but that doesn’t mean I’ve quit playing house. No, now I’m doing it on a little grander scale!</p>
      <p>To date, I’ve re-decorated my way through quite a variety of abodes: a cab over camper, a horse trailer with living quarters, an office building, various homes, a restaurant and yes, I’ve even designed what I call “Ralph Lauren” tipis at the RimRock Inn in Enterprise, Oregon! As a matter of fact, I’d probably redo the dog box, if only I could get into it!</p>
      <p>Having a small motel to redecorate has truly been a labor of love and has given me great satisfaction. I’ve tried to make Rugged Country Lodge the kind of place I love finding out on the road, but seldom do. My decorating style is influenced by many things and is tailored to the project, but certainly traveling in Europe has had a major effect. Above all else, my first priority (in wherever my decorating takes me) is to make the space feel as warm, cozy and inviting as possible.</p>
      <p><a class="btn" href="about-us.html">LEARN MORE</a></p>
    </div>
    <figure class="frame">{img(p, "jqirrhpxg7kiulznpvgr.jpeg", "An old postcard of the pioneer motel in pendleton oregon")}</figure>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>The Lodge in one Glance</h2>
    <div class="glance">{glance_html}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <div class="callout">
      <h2>Pendleton Roundup 2027</h2>
      <p>We have openings for 2027 Pendleton Roundup, if you want to inquire you can give us a call on 541-966-6800. Let'er Buck.</p>
      <p><a class="btn" href="{PHONE_TEL}">Call 541-966-6800</a></p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap reviews">
    <div>
      <h2>Guest Reviews</h2>
      <p>We strive to provide an exceptional level of service for every guest, and are proud to have a 4.4-star rating on Google.</p>
      <p>{img(p, "google.png", "The google logo is a colorful circle with a blue g in the middle.")}</p>
      <p><a class="btn" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">VIEW REVIEWS</a>
         <a class="btn btn-outline" href="{TRIPADVISOR}" target="_blank" rel="noopener">TripAdvisor</a></p>
    </div>
    <div>
      <h2>Sign Up To day</h2>
      <p>Subscribe to our newsletter and be the first to learn about our seasonal promotions and special deals.</p>
      <form data-mail="{EMAIL}" data-subject="Newsletter sign up">
        <label>Email: <input type="email" name="Email" required></label>
        <button class="btn" type="submit">Sign Up</button>
        <p class="fine">By clicking “Sign Up” I agree to the <a href="terms-privacy.html">Terms of Service</a>.</p>
      </form>
    </div>
  </div>
</section>
"""
    page(
        "index.html",
        "Rugged Country Lodge Motel | Pendleton OR Lodging",
        "Rugged country lodge is an independent motel located in Pendleton. Sparkling clean and cozy with a unique vintage charm that doesn’t cost an arm and a leg.",
        "home",
        0,
        body,
    )


def build_rooms():
    p = ""
    cards = [
        ("rooms/single-room.html", "IMG_4456-rotated.jpg", "A hotel room with a king size bed and a desk.", "Single Room"),
        ("rooms/double-room.html", "IMG_4466-rotated.jpg", "A hotel room with two beds and a television.", "Double Room"),
        ("rooms/mini-suite.html", "IMG_4450-rotated.jpg", "A hotel room with a king size bed and a television", "Mini Suite"),
        ("rooms/standard-suite.html", "IMG_4446-rotated.jpg", "A hotel room with a couch and a bed", "Standard Suite"),
    ]
    cards_html = "".join(
        f"""<article class="card">
          <a href="{href}">{img(p, src, alt)}</a>
          <div class="card-body">
            <h2>{title}</h2>
            <a class="btn" href="{href}">{title}</a>
          </div>
        </article>"""
        for href, src, alt, title in cards
    )
    body = page_hero("Rooms", bg="IMG_0278-scaled.jpg") + f"""
<section class="section">
  <div class="wrap">
    <div class="cards">{cards_html}</div>
  </div>
</section>
"""
    page(
        "rooms.html",
        "Pendleton Motel Rooms | Rugged Country Lodge",
        "View the Rooms page from Rugged Country Lodge Motel. Experience unique vintage charm. Click to view & book direct!",
        "rooms",
        0,
        body,
    )


def amenity_pills(coffee="Coffee maker"):
    return f"<h2>Amenities</h2><ul class='pills'><li>Refrigerator</li><li>Microwave</li><li>{coffee}</li></ul><p class='note'>NEWLY CARPETED THROUGHOUT THE LODGE</p>"


def build_room_pages():
    shared_hd = ROOM_SHARED.format(tv="HD television")
    shared_tcl = ROOM_SHARED.format(tv="TCL television")
    rooms = [
        (
            "rooms/single-room.html",
            "rooms-single",
            "Single Room",
            "Single Room | Pendleton | Rugged Country Lodge",
            "Enjoy a cozy single room at Rugged Country Lodge. Features vintage tiled bathrooms & quality amenities. Book your stay today!",
            "Sleeps two. One queen bed, desk and chair, double bed-side tables with lamps.",
            shared_hd,
            "Coffee maker",
            [
                ("IMG_0503-scaled.jpg", "A bedroom with a bed , dresser , desk , chair and television."),
                ("IMG_0231-scaled.jpg", "A hotel room with a bed , desk , lamp and television."),
                ("IMG_0232-scaled.jpg", "A bathroom with a sink a toilet and a mirror"),
                ("IMG_4457-rotated.jpg", "A hotel room with a king size bed and a microwave."),
                ("IMG_4461-rotated.jpg", "A bathroom with green tiles , a sink , a toilet , and a shower."),
                ("IMG_4462-rotated.jpg", "A bedroom with a bed , desk , chair , lamp and television."),
            ],
        ),
        (
            "rooms/double-room.html",
            "rooms-double",
            "Double Room",
            "Double Room | Pendleton | Rugged Country Lodge",
            "Sleeps four. Two queen beds, desk and chair, bed-side table with lamp. You'll see at a glance that we intend to be your home away from home. No lack luster, boring motel furniture here!",
            "Sleeps two. One queen bed, desk and chair, double bed-side tables with lamps.",
            shared_hd,
            "Coffee maker",
            [
                ("IMG_0234-scaled.jpg", "A hotel room with two beds and a television."),
                ("gtnidofowgobiftaeaxf-1-54c2b9c6-888ef6a2.png", "A room with a dresser and a flat screen tv"),
                ("IMG_0235-scaled.jpg", "A hotel room with two beds and a television"),
                ("IMG_05171-scaled.jpg", "A hotel room with two beds , a chair and a television."),
                ("IMG_0531-scaled.jpg", "A bathroom with green tiles , a sink , toilet and bathtub."),
                ("IMG_0525-scaled.jpg", "A hotel room with two beds , a refrigerator and a television."),
                ("IMG_4466-rotated.jpg", "A hotel room with two beds and a television."),
            ],
        ),
        (
            "rooms/mini-suite.html",
            "rooms-mini",
            "Mini Suite",
            "Mini Suite | Pendleton | Rugged Country Lodge",
            "Snugly sleeps three. One queen bed, twin sleeper couch, desk and chair, bed-side table with lamp. You'll see at a glance that we intend to be your home away from home. No lack luster, boring motel furniture here!",
            "Snugly sleeps three. One queen bed, twin sleeper couch, desk and chair, bed-side table with lamp.",
            shared_tcl,
            "Coffee Maker",
            [
                ("IMG_0233-scaled.jpg", "A hotel room with a bed , couch , table and television."),
                ("IMG_4449-rotated.jpg", "A hotel room with a king size bed , a couch , a desk , and a television"),
                ("IMG_0531-scaled.jpg", "A bathroom with green tiles , a sink , toilet and bathtub."),
                ("xigjnxleamtzdfg1t0x0.jpeg", "A bedroom with a couch a desk and a mirror"),
            ],
        ),
        (
            "rooms/standard-suite.html",
            "rooms-standard",
            "Standard Suite",
            "Standard Suite | Rugged Country Lodge | Pendleton, OR",
            "Enjoy a cozy stay in our Standard Suite with hardwood furnishings & vintage tiled bathrooms. Book your pet-friendly getaway today!",
            "Spaciously sleeps three. One queen bed, twin sleeper couch, desk and chair, bed-side table with lamp.",
            shared_hd,
            "Coffee maker",
            [
                ("IMG_4447-rotated.jpg", "A hotel room with a king size bed and a couch"),
                ("IMG_4445-rotated.jpg", "A hotel room with a couch and a bed"),
                ("IMG_05201-scaled.jpg", "A bathroom with a sink toilet and bathtub"),
            ],
        ),
    ]
    for filename, nav, heading, title, desc, intro, shared, coffee, photos in rooms:
        prefix = "../"
        body = page_hero(heading, bg=photos[0][0], prefix=prefix) + f"""
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <p class="lede">{e(intro)}</p>
      {shared}
      {amenity_pills(coffee)}
      <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book Now</a>
         <a class="btn btn-outline" href="{prefix}contact.html">Contact</a></p>
    </div>
    {room_page(photos, prefix)}
  </div>
</section>
"""
        page(filename, title, desc, nav, 1, body)


def build_about():
    p = ""
    body = page_hero("Our History", bg="IMG_0278-scaled.jpg") + f"""
<section class="section" id="OurHistory">
  <div class="wrap split">
    <div class="prose">
      <h2>What's in a name?</h2>
      <p>Back in the summer of 2003, a friend of the family visited us in Wallowa County all the way from Concrete City – Patterson, New Jersey. While camping in the Eagle Caps for the first time, wide-eyed Jimmy Nawicki awoke to God’s grandeur and penned his famous (in our circles) ‘Rugged Country’ lyrics. The male part of the Lodge’s partnership voted for ‘Rugged Country Lodge,’ remembering with a smile Jimmy’s song, while the female half wanted ‘Dream Soft’ to appeal to the more feminine side. And, after all, this sure is rugged country.</p>
      <h2>History</h2>
      <p>Rugged Country Lodge was built sometime in the 1950′s and was first known as the Pioneer Motel. When the current owners purchased it, the tired little place was being run as the Budget Inn and badly in need of some TLC.</p>
      <p>Christmas Eve of 2003, Community Bank, headquartered in Joseph, Oregon, presented a deed for the motel property to Providence Academy of Classical Christian Education, a private classical Christian school in Lostine, Oregon. The bank had repossessed the neglected motel property from its former owners before donating it to the school.</p>
      <p>Unfortunately, that winter, Pendleton experienced one of its coldest, and all of the motel’s plumbing and pipes had frozen before Providence Academy had a chance to winterize the property. Undaunted, a few naive personal investors decided to plunge ahead with the Rugged Country Lodge project anyway. We agreed to lease the motel grounds from Providence Academy and after a major and lengthy renovation, the all-new Rugged Country Lodge opened its doors to travelers in July of 2004. It has been a labor of love and an experience we wouldn’t trade–despite all the remodeling surprises along the way!</p>
      <p>Hmmmm, that is quite another story and space wouldn’t permit. Besides, we wouldn’t want people to know just how naive we were! The old saying “ignorance is bliss” is definitely true! Needless to say, countless hours were spent in trying to create a “home away from home” for the weary traveler that reflected what we wanted when we hit the road (and we do that a lot.) We wanted a place that exuded a warm yet peaceful atmosphere where our guests would become like old friends, returning many times; almost more like a bed-and-breakfast than a motel. We have always been thrilled by the prospect of finding just such a little family-owned place when we travel-–but seldom do.</p>
      <p>May our little motel be a place of peace and refuge for you, weary traveler, and may we see you many more times….Dream Soft!</p>
      <h2>Our Staff</h2>
      <p>Good help is hard to find and we are thankful to have just recently hired <span class="staff">NADEEM AKHLAQ</span> as our manager. In addition, we have a dedicated group of employees who are always willing to go the extra mile for our guests. We are so grateful for our providentially-found staff who love RCL as much as we do. They treat the Lodge like their home and our guests like their family. Without our cheerful staff, there would be no Rugged Country Lodge!</p>
    </div>
    <figure class="frame">{img(p, "jqirrhpxg7kiulznpvgr.jpeg", "An old postcard of the pioneer motel in pendleton oregon")}</figure>
  </div>
</section>
"""
    page(
        "about-us.html",
        "About Us | Rugged Country Lodge Pendleton Motel",
        "Rugged Country Lodge history, our story, amenities, and our mission statement. Visit Pendleton and stay with us!",
        "about-history",
        0,
        body,
    )


def build_story():
    p = "../"
    body = page_hero("Our Story", bg="ekmebcxfsubryajqpclw.jpeg", prefix=p) + f"""
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>Once Upon a Time</h2>
      <p>When I was a little girl I loved playing house. I spent hours fluffing pillows, picking and arranging straggly flower bouquets and constantly reorganizing my parents’ well-worn furniture. Well, I’m all grown up now, but that doesn’t mean I’ve quit playing house. No, now I’m doing it on a little grander scale!</p>
      <p>To date, I’ve re-decorated my way through quite a variety of abodes: a cab over camper, a horse trailer with living quarters, an office building, various homes, a restaurant and yes, I’ve even designed what I call “Ralph Lauren” tipis at the RimRock Inn in Enterprise, Oregon! As a matter of fact, I’d probably redo the dog box, if only I could get into it!</p>
      <p>Having a small motel to redecorate has truly been a labor of love and has given me great satisfaction. I’ve tried to make Rugged Country Lodge the kind of place I love finding out on the road, but seldom do. My decorating style is influenced by many things and is tailored to the project, but certainly traveling in Europe has had a major effect. Above all else, my first priority (in wherever my decorating takes me) is to make the space feel as warm, cozy and inviting as possible.</p>
      <h2>Office Hours</h2>
      <p>Checking in at our cozy little office is easy you will be greeted by a professionally trained staff member, eager to give you one-on-one personalized guest service–the kind found in four-and five-diamond resorts! We try our best to provide affordable places to stay in Pendleton, Oregon.</p>
      <p>Our office hours are 8AM until 10 PM. But don't worry, if you come in before or after hours, we provide a phone number for you to reach us.</p>
    </div>
    <figure class="frame">{img(p, "ekmebcxfsubryajqpclw.jpeg", "A sign for rugged country lodge dream soft")}</figure>
  </div>
</section>
"""
    page(
        "about-us/our-story.html",
        "Our Story - Rugged Country Lodge Motel - Pendleton, OR",
        "View the Our Story page from Rugged Country Lodge Motel. Experience unique vintage charm. Click to view & book direct!",
        "about-story",
        1,
        body,
    )


def build_amenities():
    p = "../"
    items = [
        ("Fine Décor", "You’ll see at a glance that we intend to be your home away from home. No lack luster, boring motel furniture here! We’ve purposely chosen Broyhill’s Attic Heirloom hardwood furnishings in an eclectic mix of colors and styles designed to make you feel right at home. Our choice of quality artwork by Albrecht Bierstadt and Thomas Moran perfectly accent our lodge style and themes of nature, so intertwined in this corner of Northeastern Oregon."),
        ("Squeaky Clean", "Entering your sparkling clean, up-scaled boutique room, you will appreciate our non-smoking policy throughout the lodge. (Tables with ashtrays are conveniently located outside.) Guests who smoke in our rooms will be charged up to a $250.00 fee."),
        ("At Your Fingertips", "Our Broyhill armoire holds a 32” crystal-clear Insignia television with over 80 cable channels. The armoire has two drawers that are ample to hold your personal belongings (after you remove the extra polar fleece blanket). For your convenience, alarm clocks, microwaves and refrigerators are found in each room and ice is always available during office hours. Our quaint vintage-tiled bathroom and fixtures are outfitted with thick, luxurious white towels, Archive Botanical Natural Bath products, a cushioned bath mat and a squeaky clean shower and tub unit. While our bathrooms and tubs are not overly large they are adequate, and period tile in contrasting colors makes them a favorite! The 1950’s renovated bathroom includes elongated toilet and a pedestal sink with a privacy window."),
        ("Dream Soft", "The best is yet to be! You would think our Spring Air Imperial Elite top-of-the-line queens (with 580 coils per inch) would be enough, but we’ve added a divinely soft two-inch platinum pillow topper, 3-4 down pillows and a 240 cotton thread count lofty blanket sandwiched between two 200 thread count, wrinkle resistant elegant tone-on-tone white sheets … now you’re definitely ready to dream soft."),
        ("Gotcha Covered", "Should you need an iron/ironing board, hair dryer or an item you may have left at home, please call our office for fast, friendly delivery to your door. We have just about everything you need, including free wireless in each room, crib and air mattress and many other extras to make you feel at home."),
        ("Rooster Room 6:30 to 9:30 am", "Our expanded, fresh breakfast is something to crow about! We proudly serve Java gourmet coffees. At 6:00 AM our gourmet coffees will aromatically draw you toward breakfast in our ‘Rooster Room,’ where fresh fruit, bread, bagels and cream cheese, cereal, oatmeal, Apple juice, orange juice and more are served until 9:00 AM. You can eat at indoor or outdoor tables or take a tray back to your room for more privacy."),
        ("Pet Friendly", "Your furry pet friends (sorry, no feathers!) are welcome at Rugged Country Lodge. However, we do charge $15.00 per pet/per night (up to two pets) since we completely strip rooms after your pet’s stay. If you have more than two pets you may call us to discuss possible options. Since we have designated pet rooms, it is vital you let us know upon booking that you have a dog. Undeclared pets will be charged $50."),
        ("Free WiFi", "Stay connected with our high speed free WIFI. We realize how important the internet is. So we are pleased to help you keep up with your online activities even when you are relaxing in one of our cozy rooms."),
        ("Ecofriendly", "As a way to do our part in reducing the carbon footprint, Rugged Country Lodge is eco-friendly. We are consciously making every effort to go “green” wherever possible."),
        ("Family Matters", "But wait—we don’t want you to be misled! With all this, you would think we were a huge chain. The truth is we’re only—after all—a family owned 28 room property completely renovated in 2004 and upgraded again in 2012. Yet, that’s the beauty of it! Though we don’t offer a fancy fitness room, Olympic-sized pool or a large convention center, we are able to offer some things those other expensive chains can’t … personalized, friendly and cheerful service in an authentic little roadside motel…the way it used to be!"),
        ("Let Us Make Your Reservations", "If you’re relaxing at the Lodge, downtown Pendleton is only minutes away with many shopping and cultural activities to pass the time. If you want to see the sights, let us give you the skinny on what’s in town to see and do. We'll happily book your reservations! We believe that nowhere else in Northeastern Oregon—or maybe anywhere—will you experience this kind of motel value. Find all this too hard to believe? We would too, but the proof is in our guest’s comments! See for yourselves what makes us stand alone and why our guests come back time and time again to their home away from home."),
        ("Be Our Guest", "We’re waiting for you, so call today or book online. Rugged Country Lodge, is Pendleton’s cutest, cleanest, most affordable motel, where our guests dream soft!"),
    ]
    arts = "".join(f"<article><h3>{e(h)}</h3><p>{e(t)}</p></article>" for h, t in items)
    body = page_hero("Amenities", bg="augtgen39rphjl2hdkpa.jpeg", prefix=p) + f"""
<section class="section">
  <div class="wrap split">
    <figure class="frame">{img(p, "augtgen39rphjl2hdkpa.jpeg", "A shower cap and a bottle of shower gel are on a towel.")}</figure>
    <figure class="frame">{img(p, "nrfj3u0q5kbh4nbeithp.png", "A kitchen with a table and chairs in front of two windows")}</figure>
  </div>
  <div class="wrap" style="margin-top:2rem">
    <div class="amenity-grid">{arts}</div>
    <p style="margin-top:1.5rem"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">BOOK NOW</a>
       <a class="btn btn-outline" href="{PHONE_TEL}">{PHONE}</a></p>
  </div>
</section>
"""
    page(
        "about-us/amenities.html",
        "Amenities - Rugged Country Lodge Motel - Pendleton, OR",
        "View the Amenities page from Rugged Country Lodge Motel. Experience unique vintage charm. Click to view & book direct!",
        "about-amenities",
        1,
        body,
    )


def build_mission():
    p = "../"
    body = page_hero("Mission Statement", bg="sh2vobmj1qx3ybaddfla.jpeg", prefix=p) + f"""
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <p>The Rugged Country Lodge has a mission to “create a home away from home.” We strive to serve you in such a way as to show our love for you by always providing sparkling clean rooms, a cozy bed and breakfast-like atmosphere where our guests are treated like friends.</p>
      <p>Through trust, integrity, and believing that others are more important than us we hope to set a new standard in the hospitality industry. It is our dream that this philosophy of excellence will impact not only our great motel, but our community and ultimately–the world.</p>
    </div>
    <figure class="frame">{img(p, "sh2vobmj1qx3ybaddfla.jpeg", "A sign for rugged country lodge is surrounded by flowers")}</figure>
  </div>
</section>
"""
    page(
        "about-us/mission-statement.html",
        "Mission Statement - Rugged Country Lodge Motel - Pendleton, OR",
        "View the Mission Statement page from Rugged Country Lodge Motel. Experience unique vintage charm. Click to view & book direct!",
        "about-mission",
        1,
        body,
    )


def build_location():
    body = page_hero("Our Location", bg="IMG_0277-scaled.jpg") + f"""
<section class="section">
  <div class="wrap">
    <h2>Points of Interest in and Around Pendleton, Oregon</h2>
    <p>Visiting Pendleton? Rugged Country Lodge recommends these things to do in the area including the best restaurants, attractions, points of interest, etc. Rugged Country Lodge is the perfect place for experiencing all that Pendleton has to offer. Stay with us and we’ll help make your visit special.</p>
    <div class="map-embed">
      <iframe src="{MAP}" title="Points of Interest in and Around Pendleton, Oregon" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p style="margin-top:1.2rem">{e(ADDR)} · <a href="{PHONE_TEL}">{PHONE}</a></p>
  </div>
</section>
"""
    page(
        "location.html",
        "Location | Rugged Country Lodge | Pendleton Oregon",
        "Visiting Pendleton? Check out our map of our recommendations for restaurants, things to do, points of interest, activities and more. Stay with us.",
        "location",
        0,
        body,
    )


def build_gallery():
    interiors = [
        ("IMG_4464-rotated.jpg", "A bedroom with a bed , desk , lamp and television."),
        ("IMG_4463-rotated.jpg", "A bedroom with a bed , dresser , nightstand and window."),
        ("waim8t2cb3fjznqfhlix.jpeg", "A bathroom with a pedestal sink and toilet"),
        ("qqul5ulotqzlh3q4ijoh.jpeg", "A bathroom with a toilet , sink and trash can."),
        ("IMG_4453-rotated.jpg", "A kitchen with wooden cabinets and shelves filled with various items"),
        ("IMG_4458.jpg", "A bathroom shelf with a towel , soap and lotion on it."),
        ("IMG_4455-rotated.jpg", "A hotel room with a king size bed and a desk"),
        ("IMG_4451-rotated.jpg", "A cereal dispenser sits on a counter in a kitchen"),
        ("IMG_4466-rotated.jpg", "A hotel room with two beds and a television."),
        ("IMG_4438.jpg", "A kitchen with a table and chairs and a microwave."),
        ("IMG_4460-rotated.jpg", "A bathroom with a sink a toilet and a bathtub"),
        ("IMG_4446-rotated.jpg", "A hotel room with a couch and a bed"),
        ("xigjnxleamtzdfg1t0x0.jpeg", "A bedroom with a couch a desk and a mirror"),
        ("IMG_4443-rotated.jpg", "A long hallway with rocking chairs and a shelf full of books."),
        ("IMG_4444-rotated.jpg", "A room with a desk and a chair in it"),
    ]
    property_shots = [
        ("bkzmea5plepydsfwf8sq.jpeg", "A motorcycle is parked in front of a building with a green roof"),
        ("jvgrmx95fijhpeepjhpx.jpeg", "A row of flowers along a sidewalk next to a parking lot"),
        ("mbn3jciixduijxmxqx4j.jpeg", "A row of flowers are growing in a planter on a sidewalk."),
        ("yhr4zimyxjsxbtfr5cjm.jpeg", "Two cars are parked in front of a building with a green roof"),
        ("xtdxxznqyccdp66rnvlb.jpeg", "A large building with a green roof and a long porch"),
        ("shg3xyf0rwlfrjj0xpgn.jpeg", "A sidewalk with flowers and a trash can on it"),
        ("nmwajfujkw2mmzi0j4sr.jpeg", "A green car is parked in a parking lot in front of a building."),
        ("kxdoku2nac3zeryjvo2g.jpeg", "A motel with a green roof and a stone wall"),
        ("rkbx2hhl1prmwiaxohyp.jpeg", "A porch with a sink and a trash can in front of a stone building."),
        ("wwmfluxfjdxch792rnui.jpeg", "A fenced in area with a bench and trees in the background"),
        ("xlfkvzyas8y7saijaj42.jpeg", "A white van is parked in a parking lot next to a stone building"),
        ("hdkofkpejcd8nkv3c0ih.jpeg", "A silver minivan is parked in a parking lot"),
        ("jbgpyhkmoszwqleiunst.jpeg", "A porch with a table and chairs and a stone wall"),
        ("IMG_4452-rotated.jpg", "A cereal dispenser sits on a counter in a kitchen"),
        ("IMG_0278-scaled.jpg", "A large building with a green roof is sitting next to a snowy road."),
        ("wxo3ogejfxayzqzod1jt.jpeg", "A white van is parked in front of a building with a green roof."),
        ("IMG_0277-scaled.jpg", "A motel with a sign that says lodge on it"),
    ]

    def grid(items):
        return "".join(
            f'<a href="images/{src}" data-lightbox>{img("", src, alt)}</a>' for src, alt in items
        )

    body = page_hero("Photo Gallery", bg="IMG_0277-scaled.jpg") + f"""
<section class="section">
  <div class="wrap">
    <div class="gallery">{grid(interiors)}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Property</h2>
    <div class="gallery">{grid(property_shots)}</div>
  </div>
</section>
"""
    page(
        "photo-gallery.html",
        "Photo Gallery | Rugged Country Lodge | Pendleton",
        "Photo gallery for Rugged Country Lodge including our rooms,common areas, the grounds, the area, and more",
        "gallery",
        0,
        body,
    )


def build_policies():
    body = page_hero("Policies") + f"""
<section class="section">
  <div class="wrap prose" style="max-width:48rem">
    <p>Rugged Country Lodge requires a 24 hour in advance cancellation policy. If you cancel less than 24 hours of your booking, your first night's rent plus applicable taxes will be applied to your credit card. Check-out time is 11:00 am and Check-in time is 03:00 pm</p>
    <p><strong>ALL</strong> of our rooms are <strong>NON SMOKING</strong>. Up to $250 in damage fees may be applied to anyone who smokes in our rooms. This policy is strictly enforced. We do allow smoking outside our building.</p>
    <p>Rugged Country Lodge is pet friendly with a non-refundable fee of $15 per pet/per night. If you have more than 2 pets, please call us to determine if we can accommodate them and what the fees would be. Should your pet do damage to a room, appropriate charges will be added to your credit card.</p>
    <p><strong>Undeclared pets are automatically charged a $50 fee. We have limited number of pet rooms please let us know while booking a room that you are travelling with a pet so that we can accommodate you , Moreover, we take dogs not the cats.</strong></p>
    <p>During Round Up cancellation require 2-weeks notice , if cancelled after that one night along with applicable taxes will be charged. Once you have a room you may not cancel at any time nor make changes. This policy is strictly enforced.</p>
    <p>If we find missing items or damage to the room after your check out, appropriate costs will be applied to your credit card.</p>
    <p>We reserve the right to refuse service to anyone for any reason.</p>
    <p>For weekly rate if you check out early (before 7-days) there will be no refund.</p>
  </div>
</section>
"""
    page(
        "policies.html",
        "Policies and Cancellations | Rugged Country Lodge",
        "General reservation information & cancellation policies for Rugged Country Lodge. Need to cancel? Please call: (541) 966-6800",
        "policies",
        0,
        body,
    )


def build_contact():
    body = page_hero("Contact Us Today") + f"""
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Contact Us</h2>
      <form data-mail="{EMAIL}" data-subject="Contact Us">
        <div class="form-row">
          <label>First Name <input type="text" name="First Name"></label>
          <label>Last Name <input type="text" name="Last Name"></label>
        </div>
        <div class="form-row">
          <label>Email <input type="email" name="Email"></label>
          <label>Phone <input type="tel" name="Phone"></label>
        </div>
        <label>Message * <textarea name="Message" required></textarea></label>
        <button class="btn" type="submit">SEND</button>
      </form>
    </div>
    <div>
      <h2>Location</h2>
      <h3>Contact details</h3>
      <p>1807 SE Court Ave<br>Pendleton, Oregon<br>97801-3348 United States</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a><br>
         <a href="{PHONE_TEL}">541-966-6800</a></p>
      <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book Now</a></p>
    </div>
  </div>
</section>
"""
    page(
        "contact.html",
        "Contact Us | Rugged Country Lodge Pendleton",
        "Contact Rugged Country Lodge 1807 SE Court Ave Pendleton, Oregon 97801 | info@ruggedcountrylodge.com / 541-966-6800",
        "contact",
        0,
        body,
    )


def build_privacy():
    body = page_hero("Terms & Privacy") + """
<section class="section">
  <div class="wrap prose" style="max-width:50rem">
    <p>Rugged Country Lodge (hereinafter “we”, “our” or “us”) is committed to maintaining your privacy. This privacy policy outlines Rugged Country Lodge's practices with respect to information collected from users who access our website at www.ruggedcountrylodge.com (“Site”), or otherwise share personal information with us. The policy also contains information about cookies. The following policies are intended to protect your privacy and ensure that your personal information is handled in a safe and responsible manner. We encourage you to refer to this policy on an ongoing basis to stay abreast of our most current privacy policy practices.</p>
    <h2>Privacy Statement</h2>
    <h3>Information We Collect</h3>
    <p>We collect two types of data and information from Users:</p>
    <p><strong>Non-personal Information</strong>. The first type of information is un-identified and non-identifiable information, which may be made available or gathered via your use of the Site. We are not aware of the identity of a User from which the Non-personal Information was collected. Non-personal Information which is being collected may include your aggregated usage information and technical information transmitted by your device, including certain software and hardware information (e.g. the type of browser and operating system your device uses, language preference, access time, etc.) in order to enhance the functionality of our Site. We may also collect information on your activity on the Site (e.g. pages viewed, online browsing, clicks, actions, etc.).</p>
    <p><strong>Personal Information.</strong> The second type of information which is individually identifiable information, namely information that identifies an individual or may with reasonable effort identify an individual. Such information includes:</p>
    <p><strong>Device Information</strong>: We collect Personal Information from your device. Such information includes geolocation data, IP address, unique identifiers (e.g. MAC address and UUID) and other information which relates to your activity through the Site.</p>
    <p><strong>Registration Information:</strong> When you sign up for a newsletter on our Site you will be asked to provide us certain details such as: full name and email.</p>
    <p><strong>Contact Information:</strong> When you fill in the Contact Us form on our Site you will be asked to provide us certain details such as: full name, phone number and email.</p>
    <p><strong>Booking Information:</strong> When making an online booking in our Booking Engine, you will be asked to provide us certain details such as: full name, contact information, demographic information, payment information. New Paragraph</p>
    <p>We receive your Personal Information from various sources:</p>
    <p>When you voluntarily provide us your personal details when filling in the form or making an online booking;</p>
    <p>When you use or access our Site in connection with your use of our services;</p>
    <p>From third party providers, services and public registers (for example, traffic analytics vendors).</p>
    <h3>Using Information</h3>
    <p>We collect two types of data and information from Users:</p>
    <p>To keep internal records;</p>
    <p>To send you notices regarding our services, provide you with technical information and responding to any customer service issue you may have;</p>
    <p>To periodically send promotional emails about new products, special offers or other information which we think you may find interesting;</p>
    <p>To serve you advertisements when you use our Site (see more under "Advertisements");</p>
    <p>To market our products (see more under "Marketing");</p>
    <p>To customize the Site according to your interests;</p>
    <p>To conduct statistical and analytical purposes, intended to improve the Site.</p>
    <h3>Advertising</h3>
    <p>We may use a third-party advertising technology to serve advertisements when you access the Site. This technology uses your information with regards to your use of the Services to serve advertisements to you (by placing third-party cookies on your web browser).</p>
    <h3>Marketing</h3>
    <p>We may use your Personal Information, such as your name, email address, telephone number, etc. ourselves or by using our third party subcontractors for the purpose of providing you with promotional materials, concerning our services, which we believe may interest you.</p>
    <p>Out of respect to your right to privacy we provide you within such marketing materials with means to decline receiving further marketing offers from us. If you unsubscribe we will remove your email address or telephone number from our marketing distribution lists.</p>
    <p>Please note that even if you have unsubscribed from receiving marketing emails from us, we may send you other types of important e-mail communications without offering you the opportunity to opt out of receiving them. These may include customer service announcements or administrative notices.</p>
    <h3>Sharing Information</h3>
    <p>We do not rent, sell, or share Users’ information with third parties except as described in this Privacy Policy. We may share your Personal Information in a limited number of circumstances, including:</p>
    <p><strong>Third-Party Service Providers</strong>: We share personal information with third parties involved in the process of providing services to you. Those third parties are only permitted to use your personal information for the purpose that it has been provided and may not disclose it to any other third party except at our express direction and in accordance with this Privacy Policy.</p>
    <p><strong>Legal &amp; Regulatory Authorities</strong>: We may share your personal information with legal and regulatory authorities or other third parties, when it is required by law, necessary to permit us to exercise our legal rights, to comply with our legal obligations, or necessary to take action regarding illegal activities or to protect the safety of any person.</p>
    <p><strong>Business Transitions</strong>: If all or part of our company is sold, merged or otherwise transferred, we may transfer your personal information as part of that transition. We may also transfer your personal data to the owners of hotels managed by us.</p>
    <h3>User Rights</h3>
    <p>You may request to:</p>
    <p>Receive confirmation as to whether or not personal information concerning you is being processed, and access your stored personal information, together with supplementary information.</p>
    <p>Receive a copy of personal information you directly volunteer to us in a structured, commonly used and machine-readable format.</p>
    <p>Request rectification of your personal information that is in our control.</p>
    <p>Request erasure of your personal information.</p>
    <p>Object to the processing of personal information by us.</p>
    <p>Request to restrict processing of your personal information by us.</p>
    <p>Lodge a complaint with a supervisory authority.</p>
    <p>However, please note that these rights are not absolute, and may be subject to our own legitimate interests and regulatory requirements.</p>
    <h3>Retention</h3>
    <p>We will retain your personal information for as long as necessary to provide our services, and as necessary to comply with our legal obligations, resolve disputes, and enforce our policies. Retention periods will be determined taking into account the type of information that is collected and the purpose for which it is collected, bearing in mind the requirements applicable to the situation and the need to destroy outdated, unused information at the earliest reasonable time. Under applicable regulations, we will keep records containing client personal data, account opening documents, communications and anything else as required by applicable laws and regulations. We may rectify, replenish or remove incomplete or inaccurate information, at any time and at our own discretion.</p>
    <h3>Security</h3>
    <p>We take great care in implementing and maintaining the security of the Site and your information. We employ industry standard procedures and policies to ensure the safety of the information we collect and retain, and prevent unauthorized use of any such information, and we require any third party to comply with similar security requirements, in accordance with this Privacy Policy. Although we take reasonable steps to safeguard information, we cannot be responsible for the acts of those who gain unauthorized access or abuse our Site, and we make no warranty, express, implied or otherwise, that we will prevent such access.</p>
    <h2>Cookie Statement</h2>
    <h3>Cookie Definition</h3>
    <p>A cookie is a small piece of information which is sent to your browser while you are viewing a website and is placed on the hard drive of your device (computer, table or smartphone). Cookies are very helpful and can be used for various different purposes. These purposes include allowing you to navigate between pages efficiently, enable automatic activation of certain features, remembering your preferences and making the interaction between you and our Services quicker and easier. Cookies are also used to help ensure that the advertisements you see are relevant to you and your interests and to compile statistical data on your use of our Services.</p>
    <h3>Types of Cookies</h3>
    <p>The Site uses the following types of cookies:</p>
    <p>'session cookies' which are stored only temporarily during a browsing session in order to allow normal use of the system and are deleted from your device when the browser is closed;</p>
    <p>'persistent cookies' which are read only by the Site, saved on your computer for a fixed period and are not deleted when the browser is closed. Such cookies are used where we need to know who you are for repeat visits, for example to allow us to store your preferences for the next sign-in;</p>
    <p>'third party cookies' which are set by other online services who run content on the page you are viewing, for example by third party analytics companies who monitor and analyze our web access.</p>
    <p>Cookies do not contain any information that personally identifies you, but Personal Information that we store about you may be linked, by us, to the information stored in and obtained from cookies.</p>
    <p>We also use a tool called “Google Analytics” to collect information about your use of the Site. Google Analytics collects information such as how often users access the Site, what pages they visit when they do so, etc. We use the information we get from Google Analytics only to improve our Site and services. Google Analytics collects the IP address assigned to you on the date you visit sites, rather than your name or other identifying information. We do not combine the information collected through the use of Google Analytics with personally identifiable information. Google’s ability to use and share information collected by Google Analytics about your visits to this Site is restricted by the Google Analytics Terms of Use and the Google Privacy Policy.</p>
    <h3>Withdrawal of Consent</h3>
    <p>You can withdraw your consent at any time by setting your browser to disable cookies or to remove all cookies from your browser by following the instructions of your device preferences. However, if you choose to disable cookies, some features of our Site may not operate properly and your online experience may be limited.</p>
    <h3>Further Information</h3>
    <p>We reserve the right to periodically amend or revise the Privacy Policy; material changes will be effective immediately upon the display of the revised Privacy policy. The last revision will be reflected in the "Last modified" section. Your continued use of the Site, following the notification of such amendments on our website, constitutes your acknowledgment and consent of such amendments to the Privacy Policy and your agreement to be bound by the terms of such amendments.</p>
    <p>If you have any general questions about the Site or the information we collect about you and how we use it, you can contact us at <a href="mailto:info@ruggedcountrylodge.com">info@ruggedcountrylodge.com</a>.</p>
    <p>Last Modified December 2024</p>
  </div>
</section>
"""
    page(
        "terms-privacy.html",
        "Privacy Statement | Rugged Country Lodge",
        "Terms of Service and privacy policy for ruggedcountrylodge.com",
        "terms",
        0,
        body,
    )


def build_a11y():
    body = page_hero("ACCESSIBILITY STATEMENT", kicker="Updated: September 2024") + f"""
<section class="section">
  <div class="wrap prose" style="max-width:50rem">
    <h2>GENERAL</h2>
    <p>Rugged Country Lodge strives to ensure that its services are accessible to people with disabilities. Rugged Country Lodge has invested a significant amount of resources in helping ensure that its website is made easier to use and more accessible for people with disabilities, with the strong belief that website accessibility efforts assist all users and that every person has the right to live with dignity, equality, comfort, and independence.</p>
    <h2>DISCLAIMER</h2>
    <p>Rugged Country Lodge continues its efforts to constantly improve the accessibility of its site and services in the belief that it is our collective moral obligation to allow seamless, accessible and unhindered use also for those of us with disabilities.</p>
    <p>Despite our efforts to make all pages and content on www.ruggedcountrylodge.com fully accessible, some content may not have yet been fully adapted to the strictest accessibility standards. This may be a result of not having found or identified the most appropriate technological solution.</p>
    <h2>HERE FOR YOU</h2>
    <p>If you are experiencing difficulty with any content on www.ruggedcountrylodge.com or require assistance with any part of our site, please contact us during normal business hours as detailed below. We will be happy to assist.</p>
    <h2>CONTACT US</h2>
    <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>
       Phone: <a href="{PHONE_TEL}">{PHONE}</a></p>
  </div>
</section>
"""
    page(
        "accessibility-statement.html",
        "Accessibility Statement - Rugged Country Lodge Motel - Pendleton, OR",
        "View the Accessibility Statement page from Rugged Country Lodge Motel. Experience unique vintage charm. Click to view & book direct!",
        "a11y",
        0,
        body,
    )


if __name__ == "__main__":
    build_home()
    build_rooms()
    build_room_pages()
    build_about()
    build_story()
    build_amenities()
    build_mission()
    build_location()
    build_gallery()
    build_policies()
    build_contact()
    build_privacy()
    build_a11y()
