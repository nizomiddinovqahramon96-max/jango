from django.shortcuts import render

PROFILE = {
    "name": "Qahramon Nizomiddinov",
    "role": "Python Developer va Student",
    "age": "17",
    "school": "281-maktab o'quvchisiman",
    "center": "Mars IT markazida dasturlashni o'rganaman",
    "goal": "Kelajakda kuchli Backend Developer bo'lishni maqsad qilganman.",
    "interests": ["Boks", "Armrestling"],
    "instagram": "@qahramon.uzb",
    "instagram_url": "https://www.instagram.com/qahramon.uzb/",
}

SKILLS = ["Python", "Django", "HTML", "CSS"]

PROJECTS = [
    {
        "title": "Telefon Narxlash",
        "short": "Telefon modellari va narxlarni bir joyda solishtirish uchun tayyorlangan loyiha.",
        "description": "Foydalanuvchi telefon nomini tanlab, narx va asosiy xususiyatlarini tez ko'radi.",
        "stack": ["Python", "HTML", "CSS"],
        "features": ["Telefonlar ro'yxati", "Narx solishtirish", "Responsive kartochkalar"],
    },
    {
        "title": "Market Magazin",
        "short": "Oddiy mahsulot katalogi, savatcha va buyurtma jarayonini o'rgatuvchi loyiha.",
        "description": "Mahsulotlarni ko'rish, tanlash va savatchaga qo'shish orqali online magazin mantiqini o'zlashtiradi.",
        "stack": ["Python", "Django", "HTML", "CSS"],
        "features": ["Mahsulotlar katalogi", "Savatcha mantiqi", "Toza interfeys"],
    },
    {
        "title": "Not Coin",
        "short": "Telegram uslubidagi interaktiv loyiha konsepsiyasi.",
        "description": "Bosish, ball yig'ish va natijani kuzatish orqali oddiy interaktiv mexanikani ko'rsatadi.",
        "stack": ["Python", "HTML", "CSS"],
        "features": ["Interaktiv bosish", "Ball hisobi", "Minimal dizayn"],
    },
]

POSTS = [
    {
        "year": 2026,
        "month": "Iyun",
        "date": "18 Iyun, 2026",
        "sort": 20260618,
        "title": "Django bilan portfolio sayt yaratish",
        "summary": "Template inheritance, static fayllar va responsive dizayn yordamida toza portfolio sayt qurish yo'li.",
        "tag": "Django",
    },
    {
        "year": 2026,
        "month": "Iyun",
        "date": "12 Iyun, 2026",
        "sort": 20260612,
        "title": "Python developer bo'lish uchun birinchi 5 qadam",
        "summary": "Python, Django, HTML va CSS ni ketma-ket o'rganib, real loyiha qilish rejasini tuzish.",
        "tag": "Python",
    },
    {
        "year": 2026,
        "month": "May",
        "date": "24 May, 2026",
        "sort": 20260524,
        "title": "HTML va CSS da toza interfeys",
        "summary": "Kulrang fon, kartochkalar, tipografiya va animatsiyalar yordamida professional sahifa yaratish.",
        "tag": "Frontend",
    },
    {
        "year": 2025,
        "month": "Dekabr",
        "date": "16 Dekabr, 2025",
        "sort": 20251216,
        "title": "Backend developer bo'lishda Django nega muhim",
        "summary": "Django orqali URL, view, template va static fayllar bilan ishlaydigan to'liq web loyiha qurish.",
        "tag": "Backend",
    },
    {
        "year": 2025,
        "month": "Oktyabr",
        "date": "08 Oktyabr, 2025",
        "sort": 20251008,
        "title": "Market Magazin loyihasidan olgan saboqlar",
        "summary": "Mahsulot, savatcha va foydalanuvchi tajribasi haqida oddiy, lekin foydali xulosalar.",
        "tag": "Loyiha",
    },
    {
        "year": 2024,
        "month": "Dekabr",
        "date": "20 Dekabr, 2024",
        "sort": 20241220,
        "title": "Telefon Narxlash loyihasini qanday qildim",
        "summary": "Oddiy ma'lumotlarni chiroyli kartochkaga aylantirish va responsive qilish tajribasi.",
        "tag": "Loyiha",
    },
    {
        "year": 2024,
        "month": "Sentyabr",
        "date": "14 Sentyabr, 2024",
        "sort": 20240914,
        "title": "Not Coin loyihasida interaktivlik",
        "summary": "Oddiy bosish mexanikasi orqali foydalanuvchi harakatini qiziqarli qilish usullari.",
        "tag": "Frontend",
    },
    {
        "year": 2024,
        "month": "Iyun",
        "date": "03 Iyun, 2024",
        "sort": 20240603,
        "title": "Mars IT da dasturlashni o'rganish",
        "summary": "Dasturlashni noldan boshlab, amaliy loyihalar orqali oldinga siljish haqida qisqa xotira.",
        "tag": "O'qish",
    },
]

PAGE_INFO = {
    "home": {
        "title": "Qahramon Nizomiddinov — Python Developer va Student",
        "description": "Qahramon Nizomiddinovning Python, Django, HTML va CSS bilan yaratilgan portfolio va blog sahifasi.",
    },
    "about": {
        "title": "Mening haqimda — Qahramon Nizomiddinov",
        "description": "Qahramon Nizomiddinov haqida: yosh, o'qish, Mars IT markazi, ko'nikmalar va maqsadlar.",
    },
    "projects": {
        "title": "Loyihalar — Qahramon Nizomiddinov",
        "description": "Telefon Narxlash, Market Magazin va Not Coin loyihalari haqida ma'lumot.",
    },
    "blog": {
        "title": "Blog — Qahramon Nizomiddinov",
        "description": "Python, Django, frontend va loyiha tajribalari haqida blog yozuvlari.",
    },
}


def _context(page):
    info = PAGE_INFO[page]
    sorted_posts = sorted(POSTS, key=lambda post: post["sort"], reverse=True)
    grouped_posts = {}

    for post in sorted_posts:
        grouped_posts.setdefault(post["year"], {}).setdefault(post["month"], []).append(post)

    blog_groups = [
        {
            "year": year,
            "months": [
                {"name": month, "posts": month_posts}
                for month, month_posts in months.items()
            ],
        }
        for year, months in grouped_posts.items()
    ]

    return {
        "profile": PROFILE,
        "skills": SKILLS,
        "projects": PROJECTS,
        "latest_posts": sorted_posts[:4],
        "blog_groups": blog_groups,
        "active": page,
        "page_title": info["title"],
        "meta_description": info["description"],
    }


def home(request):
    return render(request, "home.html", _context("home"))


def about(request):
    return render(request, "about.html", _context("about"))


def projects(request):
    return render(request, "projects.html", _context("projects"))


def blog(request):
    return render(request, "blog.html", _context("blog"))
