import streamlit as st
from pathlib import Path
import base64
import urllib.parse

# =========================================================
# DIRECTORIES
# =========================================================

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

BACKGROUND_DIR = ASSETS / "background"
PROFILE_DIR = ASSETS / "profile"
INDICATOR_DIR = ASSETS / "indicator"
TESTIMONIAL_DIR = ASSETS / "testimonials"
VIDEO_DIR = ASSETS / "videos"
BROKER_DIR = ASSETS / "broker"

LOGO_FILE = ASSETS / "logo.png"

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".webm"
}


# =========================================================
# CONFIG
# =========================================================

if LOGO_FILE.exists():

    st.set_page_config(
        page_title="Aditya X Indicators",
        page_icon=str(LOGO_FILE),
        layout="wide",
        initial_sidebar_state="collapsed"
    )

else:

    st.set_page_config(
        page_title="Aditya X Indicators",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed"
    )


# =========================================================
# WHATSAPP
# =========================================================

WHATSAPP_NUMBER = "62859106510397"

WHATSAPP_MESSAGE = (
    "Halo Kak Aditya, saya tertarik dengan Aditya X Indicators. "
    "Saya ingin mengetahui informasi mengenai indicator "
    "dan private learning."
)

WHATSAPP_URL = (
    "https://wa.me/"
    + WHATSAPP_NUMBER
    + "?text="
    + urllib.parse.quote(WHATSAPP_MESSAGE)
)


# =========================================================
# GOOGLE DRIVE
# =========================================================

DRIVE_URL = (
    "https://drive.google.com/drive/folders/"
    "17tB7rubdImMS1yZ2XVyhS_v0hQSL_iRd"
)


# =========================================================
# MAXCO REGISTRATION
# =========================================================

MAXCO_REGISTER_URL = (
    "https://ct.maxco.co.id/register?share=9L-JEaaMp5"
)


# =========================================================
# HELPERS
# =========================================================

def get_images(folder):

    if not folder.exists():
        return []

    return sorted(
        [
            x
            for x in folder.iterdir()
            if x.is_file()
            and x.suffix.lower() in IMAGE_EXTENSIONS
        ]
    )


def get_videos(folder):

    if not folder.exists():
        return []

    return sorted(
        [
            x
            for x in folder.iterdir()
            if x.is_file()
            and x.suffix.lower() in VIDEO_EXTENSIONS
        ]
    )


def image_to_base64(path):

    with open(path, "rb") as file:
        encoded = base64.b64encode(
            file.read()
        ).decode()

    extension = path.suffix.lower()

    if extension == ".png":
        mime = "image/png"

    elif extension == ".webp":
        mime = "image/webp"

    else:
        mime = "image/jpeg"

    return f"data:{mime};base64,{encoded}"


def video_to_base64(path):

    with open(path, "rb") as file:
        encoded = base64.b64encode(
            file.read()
        ).decode()

    extension = path.suffix.lower()

    if extension == ".webm":
        mime = "video/webm"

    elif extension == ".mov":
        mime = "video/quicktime"

    else:
        mime = "video/mp4"

    return f"data:{mime};base64,{encoded}"


# =========================================================
# BACKGROUND
# =========================================================

backgrounds = get_images(BACKGROUND_DIR)

if backgrounds:

    background_url = image_to_base64(
        backgrounds[0]
    )

    background_css = f"""
        background-image:
            linear-gradient(
                rgba(3, 8, 15, 0.88),
                rgba(3, 8, 15, 0.96)
            ),
            url("{background_url}");

        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    """

else:

    background_css = """
        background:
            radial-gradient(
                circle at top,
                rgba(0, 230, 168, 0.12),
                transparent 40%
            ),
            #050a11;
    """


# =========================================================
# GLOBAL CSS
# =========================================================

st.html(
    f"""
    <style>

    html {{
        scroll-behavior: smooth;
    }}

    body {{
        margin: 0;
    }}

    .stApp {{
        {background_css}
        color: #f4f7fb;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    [data-testid="stToolbar"] {{
        display: none;
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 5rem !important;
        padding-bottom: 5rem !important;
    }}


    /* =====================================================
       TEXT
       ===================================================== */

    .brand {{
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 1px;
        white-space: nowrap;
    }}

    .brand-x {{
        color: #00e6a8;
    }}

    .nav-text {{
        color: #7f8da1;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.2px;
        text-align: right;
    }}

    .eyebrow {{
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid rgba(0,230,168,.25);
        background: rgba(0,230,168,.07);
        color: #00e6a8;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 1.5px;
    }}

    .hero-title {{
        margin-top: 22px;
        font-size: clamp(48px, 7vw, 82px);
        line-height: 0.98;
        letter-spacing: -4px;
        font-weight: 950;
        color: #f7fafc;
    }}

    .hero-title span {{
        color: #00e6a8;
    }}

    .hero-subtitle {{
        margin-top: 22px;
        max-width: 680px;
        color: #a6b2c2;
        font-size: 17px;
        line-height: 1.8;
    }}

    .section-label {{
        color: #00e6a8;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }}

    .section-title {{
        font-size: clamp(32px, 4vw, 50px);
        line-height: 1.1;
        font-weight: 950;
        letter-spacing: -2px;
        color: #f7fafc;
        margin-bottom: 14px;
    }}

    .section-text {{
        color: #93a1b3;
        line-height: 1.8;
        max-width: 720px;
    }}


    /* =====================================================
       CARDS
       ===================================================== */

    .uniform-card {{
        box-sizing: border-box;
        height: 255px;
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,.08);

        background:
            linear-gradient(
                145deg,
                rgba(13,23,36,.90),
                rgba(5,10,17,.90)
            );

        box-shadow:
            0 20px 60px rgba(0,0,0,.22);

        backdrop-filter: blur(12px);
    }}

    .card-icon {{
        font-size: 34px;
        margin-bottom: 18px;
    }}

    .card-title {{
        color: #f5f8fb;
        font-size: 20px;
        font-weight: 900;
        margin-bottom: 12px;
    }}

    .card-text {{
        color: #93a1b3;
        font-size: 14px;
        line-height: 1.75;
    }}


    /* =====================================================
       PROFILE
       ===================================================== */

    .profile-card {{
        box-sizing: border-box;
        padding: 25px;
        border-radius: 22px;
        border: 1px solid rgba(255,255,255,.08);
        background: rgba(8,15,25,.88);
        text-align: center;
        backdrop-filter: blur(15px);
    }}

    .profile-name {{
        margin-top: 16px;
        color: #ffffff;
        font-size: 24px;
        font-weight: 900;
    }}

    .profile-role {{
        margin-top: 7px;
        color: #00e6a8;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 2px;
    }}


    /* =====================================================
       STATS
       ===================================================== */

    .stat-card {{
        box-sizing: border-box;
        height: 140px;
        padding: 24px 15px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,.07);
        background: rgba(7,14,24,.85);
        text-align: center;
    }}

    .stat-number {{
        color: #00e6a8;
        font-size: 30px;
        font-weight: 950;
    }}

    .stat-label {{
        color: #8492a5;
        font-size: 12px;
        margin-top: 8px;
    }}


    /* =====================================================
       PACKAGE
       ===================================================== */

    .package-card {{
        box-sizing: border-box;
        min-height: 410px;
        padding: 34px;
        border-radius: 22px;
        border: 1px solid rgba(0,230,168,.22);

        background:
            linear-gradient(
                145deg,
                rgba(0,230,168,.10),
                rgba(5,12,20,.92)
            );
    }}

    .price {{
        color: #00e6a8;
        font-size: 60px;
        line-height: 1;
        font-weight: 950;
        letter-spacing: -3px;
    }}

    .price-sub {{
        color: #7f8da1;
        margin-top: 8px;
        font-size: 13px;
    }}


    /* =====================================================
       BROKER
       ===================================================== */

    .broker-card {{
        box-sizing: border-box;
        min-height: 400px;
        padding: 32px;
        border-radius: 22px;
        border: 1px solid rgba(255,255,255,.08);
        background: rgba(7,14,24,.90);
    }}

    .broker-title {{
        color: #ffffff;
        font-size: 32px;
        font-weight: 950;
    }}

    .broker-title span {{
        color: #00e6a8;
    }}

    .broker-check {{
        color: #d7e0ea;
        font-size: 14px;
        margin: 13px 0;
    }}


    /* =====================================================
       BONUS
       ===================================================== */

    .bonus-card {{
        box-sizing: border-box;
        padding: 35px;
        border-radius: 22px;
        border: 1px solid rgba(0,230,168,.18);
        background: rgba(0,230,168,.045);
    }}


    /* =====================================================
       CTA
       ===================================================== */

    .cta-card {{
        box-sizing: border-box;
        padding: 55px 30px;
        border-radius: 25px;
        text-align: center;
        border: 1px solid rgba(0,230,168,.18);

        background:
            radial-gradient(
                circle at center,
                rgba(0,230,168,.12),
                rgba(5,10,17,.95) 65%
            );
    }}


    /* =====================================================
       IMAGE
       ===================================================== */

    .showcase-image {{
        width: 100%;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,.08);
        display: block;
    }}


    /* =====================================================
       PORTRAIT VIDEO 9:16
       ===================================================== */

    .video-wrapper {{
        width: 100%;
        aspect-ratio: 9 / 16;

        position: relative;

        border-radius: 18px;
        overflow: hidden;

        border: 1px solid rgba(255,255,255,.08);

        background: #050a11;

        box-shadow:
            0 20px 50px rgba(0,0,0,.25);

        margin-bottom: 20px;
    }}

    .video-wrapper video {{
        width: 100%;
        height: 100%;

        display: block;

        object-fit: contain;

        background: #050a11;
    }}


    /* =====================================================
       WHATSAPP
       ===================================================== */

    .wa-floating {{
        position: fixed;
        right: 25px;
        bottom: 25px;

        width: 62px;
        height: 62px;

        border-radius: 50%;

        background: #25D366;

        display: flex;
        align-items: center;
        justify-content: center;

        text-decoration: none;

        box-shadow:
            0 12px 35px rgba(0,0,0,.35);

        z-index: 99999;

        transition: .2s;
    }}

    .wa-floating:hover {{
        transform: scale(1.08);
    }}

    .wa-icon {{
        width: 34px;
        height: 34px;
    }}


    /* =====================================================
       MOBILE
       ===================================================== */

    @media(max-width: 768px) {{

        .block-container {{
            padding-top: 4rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }}

        .hero-title {{
            font-size: 50px;
            letter-spacing: -2.5px;
        }}

        .uniform-card {{
            height: auto;
            min-height: 255px;
            margin-bottom: 15px;
        }}

        .stat-card {{
            margin-bottom: 12px;
        }}

        .video-wrapper {{
            aspect-ratio: 9 / 16;
            margin-bottom: 20px;
        }}

        .wa-floating {{
            width: 56px;
            height: 56px;
            right: 18px;
            bottom: 18px;
        }}

        .brand {{
            font-size: 17px;
        }}

        .navbar-logo {{
            width: 34px !important;
            height: 34px !important;
        }}

        .nav-text {{
            font-size: 8px;
        }}

    }}

    </style>
    """
)


# =========================================================
# NAVBAR
# =========================================================

nav1, nav2, nav3 = st.columns(
    [2, 1, 1]
)

with nav1:

    if LOGO_FILE.exists():

        logo_base64 = image_to_base64(
            LOGO_FILE
        )

        st.html(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                min-height:45px;
            ">

                <img
                    src="{logo_base64}"
                    class="navbar-logo"
                    style="
                        width:42px;
                        height:42px;
                        object-fit:contain;
                        border-radius:10px;
                    "
                >

                <div class="brand">
                    ADITYA
                    <span class="brand-x">X</span>
                    INDICATORS
                </div>

            </div>
            """
        )

    else:

        st.html(
            """
            <div class="brand">
                ADITYA
                <span class="brand-x">X</span>
                INDICATORS
            </div>
            """
        )


with nav2:

    st.html(
        """
        <div class="nav-text">
            MT4 PC • MT4 MOBILE
        </div>
        """
    )


with nav3:

    st.html(
        """
        <div class="nav-text">
            PRIVATE TRADING EDUCATION
        </div>
        """
    )


st.write("")


# =========================================================
# HERO
# =========================================================

hero_left, hero_right = st.columns(
    [1.3, .7],
    gap="large"
)

with hero_left:

    st.html(
        """
        <div class="eyebrow">
            ⚡ TRADING INDICATOR • EDUCATION • SIGNAL
        </div>

        <div class="hero-title">
            Belajar Trading<br>
            Cara <span>Simple.</span>
        </div>

        <div class="hero-subtitle">
            Pelajari cara menggunakan trading indicator
            dengan pembelajaran privat secara langsung
            melalui laptop Anda.
            <br><br>
            Berpengalaman sejak 2019 dalam edukasi trading
            dan telah membantu ratusan trader memahami
            cara trading hingga lebih mandiri.
        </div>
        """
    )

    st.write("")

    a, b = st.columns(2)

    with a:

        st.html(
            """
            <div class="uniform-card" style="height:140px;">
                <div class="card-icon">🖥️</div>

                <div class="card-title">
                    MetaTrader 4
                </div>

                <div class="card-text">
                    PC / Laptop
                </div>
            </div>
            """
        )

    with b:

        st.html(
            """
            <div class="uniform-card" style="height:140px;">
                <div class="card-icon">📱</div>

                <div class="card-title">
                    MetaTrader 4
                </div>

                <div class="card-text">
                    Mobile / HP
                </div>
            </div>
            """
        )

    st.write("")

    st.link_button(
        "💬 Konsultasi via WhatsApp",
        WHATSAPP_URL
    )


with hero_right:

    profiles = get_images(PROFILE_DIR)

    if profiles:

        st.image(
            str(profiles[0]),
            use_container_width=True
        )

    st.html(
        """
        <div class="profile-card">

            <div class="profile-name">
                Aditya X Indicators
            </div>

            <div class="profile-role">
                TRADING EDUCATION
            </div>

        </div>
        """
    )


# =========================================================
# STATS
# =========================================================

st.divider()

stats = [
    ("2019", "Berpengalaman Sejak"),
    ("100+", "Trader Dibantu"),
    ("MT4", "Platform"),
    ("Rp500K", "Sekali Bayar")
]

columns = st.columns(4)

for column, (number, label) in zip(
    columns,
    stats
):

    with column:

        st.html(
            f"""
            <div class="stat-card">

                <div class="stat-number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """
        )


# =========================================================
# WHAT YOU GET
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        WHAT YOU GET
    </div>

    <div class="section-title">
        Lebih dari Sekadar Indicator
    </div>

    <div class="section-text">
        Anda mendapatkan indicator sekaligus
        pembelajaran privat mengenai cara menggunakan
        alat tersebut.
    </div>
    """
)

st.write("")

features = [

    (
        "📊",
        "Trading Indicator",
        "Mendapatkan indicator penghasil signal yang telah digunakan sejak 2019."
    ),

    (
        "📱",
        "Telegram Signal",
        "Bonus akses channel signal Telegram."
    ),

    (
        "👨‍🏫",
        "Private Learning",
        "Bimbingan trading secara privat hingga memahami penggunaan indicator secara mandiri."
    )
]

columns = st.columns(3)

for column, (
    icon,
    title,
    text
) in zip(
    columns,
    features
):

    with column:

        st.html(
            f"""
            <div class="uniform-card">

                <div class="card-icon">
                    {icon}
                </div>

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {text}
                </div>

            </div>
            """
        )


# =========================================================
# INDICATOR SHOWCASE
# =========================================================

indicator_images = get_images(
    INDICATOR_DIR
)

if indicator_images:

    st.divider()

    st.html(
        """
        <div class="section-label">
            INDICATOR SHOWCASE
        </div>

        <div class="section-title">
            Lihat Cara Kerjanya
        </div>

        <div class="section-text">
            Contoh tampilan trading indicator
            pada MetaTrader 4.
        </div>
        """
    )

    st.write("")

    for i in range(
        0,
        len(indicator_images),
        3
    ):

        row = indicator_images[i:i + 3]

        columns = st.columns(3)

        for column, image in zip(
            columns,
            row
        ):

            with column:

                st.image(
                    str(image),
                    use_container_width=True
                )


# =========================================================
# PRIVATE PACKAGE
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        PRIVATE PACKAGE
    </div>

    <div class="section-title">
        Belajar Secara Privat
    </div>
    """
)

package1, package2 = st.columns(
    [1.15, .85],
    gap="large"
)

with package1:

    st.html(
        """
        <div class="uniform-card"
             style="height:410px;">

            <div class="card-icon">
                🎓
            </div>

            <div class="card-title">
                Private Trading Learning
            </div>

            <div class="card-text">

                Pembelajaran dilakukan secara full privat
                menggunakan laptop Anda.

                <br><br>

                💻 Remote menggunakan AnyDesk

                <br><br>

                ✓ Menjelaskan langsung pada layar laptop Anda
                <br>
                ✓ Setiap langkah trading dijelaskan
                <br>
                ✓ Pemasangan indicator dilakukan langsung
                <br>
                ✓ Menjelaskan penggunaan indicator
                <br>
                ✓ Interaktif dan dapat bertanya langsung
                <br>
                ✓ Dibimbing hingga lebih mandiri

            </div>

        </div>
        """
    )


with package2:

    st.html(
        """
        <div class="package-card">

            <div class="section-label">
                PRIVATE PACKAGE
            </div>

            <div class="price">
                Rp500K
            </div>

            <div class="price-sub">
                Sekali bayar
            </div>

            <br>

            <div class="card-text">

                ✓ Trading Indicator
                <br><br>

                ✓ Private Learning
                <br><br>

                ✓ Bonus Telegram Signal
                <br><br>

                ✓ Pemasangan indicator
                <br><br>

                ✓ Panduan penggunaan

            </div>

        </div>
        """
    )

    st.write("")

    st.link_button(
        "💬 Saya Berminat",
        WHATSAPP_URL,
        use_container_width=True
    )


# =========================================================
# TESTIMONIAL
# =========================================================

testimonial_images = get_images(
    TESTIMONIAL_DIR
)

st.divider()

st.html(
    """
    <div class="section-label">
        SOCIAL PROOF
    </div>

    <div class="section-title">
        Testimoni Nasabah
    </div>

    <div class="section-text">
        Dokumentasi testimoni dari pengguna yang
        telah mengikuti pembelajaran.
    </div>
    """
)

st.write("")

if testimonial_images:

    for i in range(
        0,
        len(testimonial_images),
        3
    ):

        row = testimonial_images[i:i + 3]

        columns = st.columns(3)

        for column, image in zip(
            columns,
            row
        ):

            with column:

                st.image(
                    str(image),
                    use_container_width=True
                )

else:

    st.caption(
        "Foto testimoni akan muncul otomatis "
        "setelah dimasukkan ke assets/testimonials/."
    )


# =========================================================
# VIDEO PORTRAIT
# =========================================================

videos = get_videos(
    VIDEO_DIR
)

if videos:

    st.divider()

    st.html(
        """
        <div class="section-label">
            VIDEO
        </div>

        <div class="section-title">
            Testimoni Video
        </div>

        <div class="section-text">
            Dokumentasi video testimoni dari pengguna
            yang telah mengikuti pembelajaran.
        </div>
        """
    )

    st.write("")

    for i in range(
        0,
        len(videos),
        2
    ):

        row = videos[i:i + 2]

        columns = st.columns(
            2,
            gap="large"
        )

        for column, video in zip(
            columns,
            row
        ):

            with column:

                try:

                    video_data = video_to_base64(
                        video
                    )

                    st.html(
                        f"""
                        <div class="video-wrapper">

                            <video
                                controls
                                playsinline
                                preload="metadata"
                            >

                                <source
                                    src="{video_data}"
                                    type="video/mp4"
                                >

                                Browser Anda tidak
                                mendukung video HTML5.

                            </video>

                        </div>
                        """
                    )

                except Exception:

                    st.error(
                        f"Video gagal dimuat: {video.name}"
                    )


# =========================================================
# BROKER
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        BROKER PARTNER
    </div>

    <div class="section-title">
        Maxco by Panin
    </div>
    """
)

broker1, broker2 = st.columns(
    [1.15, .85],
    gap="large"
)

with broker1:

    st.html(
        """
        <div class="broker-card">

            <div class="broker-title">
                MAXCO
                <span>BY PANIN</span>
            </div>

            <br>

            <div class="card-text">

                Kami menggunakan Maxco sebagai broker
                partner untuk kebutuhan trading.

                <br><br>

                <div class="broker-check">
                    ✓ Legal & Diawasi BAPPEBTI
                </div>

                <div class="broker-check">
                    ✓ Spread rendah
                </div>

                <div class="broker-check">
                    ✓ Komisi $1 / 1 lot
                </div>

                <div class="broker-check">
                    ✓ Layanan deposit & withdrawal
                </div>

                <div class="broker-check">
                    ✓ Pendampingan dan edukasi trading personal
                </div>

            </div>

        </div>
        """
    )


with broker2:

    broker_images = get_images(
        BROKER_DIR
    )

    if broker_images:

        st.image(
            str(broker_images[0]),
            use_container_width=True
        )

    else:

        st.html(
            """
            <div class="broker-card">

                <div class="card-icon">
                    🏦
                </div>

                <div class="card-title">
                    Maxco by Panin
                </div>

                <div class="card-text">
                    Masukkan gambar broker
                    ke assets/broker/
                </div>

            </div>
            """
        )


# =========================================================
# BONUS
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        SPECIAL BONUS
    </div>

    <div class="section-title">
        Bonus Indicator
    </div>

    <div class="bonus-card">

        <div class="card-title">
            🎁 Trading melalui Broker Partner
        </div>

        <div class="card-text">

            Bagi Anda yang mendaftar dan melakukan
            transaksi melalui broker yang kami gunakan,
            tersedia bonus 1 trading indicator.

            <br><br>

            Indicator bonus hanya aktif selama akun
            masih menggunakan broker partner sesuai
            dengan ketentuan yang berlaku.

        </div>

    </div>
    """
)


# =========================================================
# GUIDE
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        GET STARTED
    </div>

    <div class="section-title">
        Panduan Pendaftaran MAXCO
    </div>

    <div class="section-text">
        Semua tutorial pendaftaran telah disiapkan
        dalam bentuk PDF lengkap dengan gambar
        dan langkah-langkah detail.
    </div>
    """
)

st.write("")

steps = [

    (
        "01",
        "Akun Demo",
        "Membuat akun Demo terlebih dahulu."
    ),

    (
        "02",
        "Transaksi Demo",
        "Melakukan minimal 1x open posisi."
    ),

    (
        "03",
        "Akun Real",
        "Melanjutkan proses pembuatan akun Real."
    ),

    (
        "04",
        "Trading",
        "Mengikuti Trading Rules dan panduan."
    )

]

columns = st.columns(4)

for column, (
    number,
    title,
    description
) in zip(
    columns,
    steps
):

    with column:

        st.html(
            f"""
            <div class="uniform-card">

                <div class="section-label">
                    {number}
                </div>

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {description}
                </div>

            </div>
            """
        )


# =========================================================
# MAXCO REGISTRATION BUTTON
# =========================================================

st.write("")

st.link_button(
    "📝 DAFTAR AKUN DEMO MAXCO",
    MAXCO_REGISTER_URL,
    use_container_width=True
)

st.write("")

st.info(
    "Penting: Silakan melakukan pendaftaran akun MAXCO "
    "melalui tombol di atas agar pendaftaran terhubung "
    "dengan referral kami."
)

st.write("")

st.link_button(
    "📖 BUKA PANDUAN PENDAFTARAN MAXCO",
    DRIVE_URL,
    use_container_width=True
)


# =========================================================
# FAQ
# =========================================================

st.divider()

st.html(
    """
    <div class="section-label">
        FAQ
    </div>

    <div class="section-title">
        Pertanyaan yang Sering Ditanyakan
    </div>
    """
)

faq = {

    "Apakah cocok untuk pemula?":

        """
        Pembelajaran dilakukan secara privat sehingga
        materi dapat disesuaikan dengan tingkat pemahaman
        peserta.
        """,

    "Platform apa yang digunakan?":

        """
        Indicator digunakan pada MetaTrader 4.
        """,

    "Bagaimana proses pemasangan indicator?":

        """
        Pemasangan dilakukan secara langsung melalui
        remote menggunakan AnyDesk.
        """,

    "Berapa harga indicator?":

        """
        Paket private learning dan indicator tersedia
        dengan harga Rp500.000 sekali bayar.
        """,

    "Apakah mendapatkan signal Telegram?":

        """
        Ya. Channel signal Telegram diberikan sebagai
        bonus sesuai paket yang ditawarkan.
        """,

    "Bagaimana mendapatkan bonus indicator?":

        """
        Bonus diberikan kepada pengguna yang mendaftar
        dan melakukan transaksi melalui broker partner
        sesuai dengan ketentuan yang berlaku.
        """
}

for question, answer in faq.items():

    with st.expander(question):

        st.write(answer)


# =========================================================
# CTA
# =========================================================

st.divider()

st.html(
    """
    <div class="cta-card">

        <div class="section-label">
            READY TO START?
        </div>

        <div class="section-title">
            Siap Belajar Trading
            Cara Simple?
        </div>

        <div class="section-text"
             style="margin:auto;">

            Dapatkan indicator, private learning,
            dan bonus Telegram Signal.

        </div>

    </div>
    """
)

st.write("")

st.link_button(
    "💬 HUBUNGI ADITYA VIA WHATSAPP",
    WHATSAPP_URL,
    use_container_width=True
)


# =========================================================
# DISCLAIMER
# =========================================================

st.divider()

st.warning(
    """
    ⚠️ Risk Disclaimer

    Trading memiliki risiko dan tidak ada indicator,
    strategi, atau metode trading yang dapat menjamin
    keuntungan.

    Hasil trading setiap individu dapat berbeda tergantung
    kondisi pasar, strategi, manajemen risiko, dan faktor
    lainnya.

    Materi pada website ini ditujukan untuk edukasi dan
    informasi mengenai penggunaan indicator.

    Pastikan memahami risiko sebelum melakukan transaksi.
    """
)


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div style="
        text-align:center;
        padding:30px 0 15px 0;
    ">

        <div style="
            font-size:21px;
            font-weight:950;
        ">

            ADITYA
            <span style="color:#00e6a8;">
                X
            </span>
            INDICATORS

        </div>

        <div style="
            color:#718096;
            font-size:12px;
            margin-top:10px;
        ">

            Trading Education • Indicator • Private Learning

        </div>

        <div style="
            color:#4e5b6d;
            font-size:11px;
            margin-top:18px;
        ">

            © 2026 Aditya X Indicators.
            All rights reserved.

        </div>

        <div style="
            color:#4e5b6d;
            font-size:10px;
            margin-top:5px;
        ">

            Trading involves substantial risk.
            Trade responsibly.

        </div>

    </div>
    """
)


# =========================================================
# FLOATING WHATSAPP
# =========================================================

# Gunakan SVG sebagai gambar (data URI), bukan inline <svg>.
# Ini lebih kompatibel dengan st.html/Streamlit sehingga logo WA
# tetap muncul di dalam tombol hijau.
WA_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<path fill="white" d="M16 3C8.82 3 3 8.82 3 16c0 2.29.7 4.42 1.86 6.19L3.07 28.93l6.91-1.81A13.7 13.7 0 0 0 16 28.83C23.18 28.83 29 23.01 29 15.83 29 8.65 23.18 3 16 3Zm0 23.55c-2.05 0-4.05-.55-5.79-1.6l-.41-.25-4.1 1.08 1.1-4-.27-.42A10.95 10.95 0 0 1 5 15.83C5 9.78 9.95 4.83 16 4.83s11 4.95 11 11-4.95 10.72-11 10.72Zm6.36-8.03c-.35-.18-2.07-1.02-2.39-1.13-.32-.12-.55-.18-.78.18-.23.35-.9 1.13-1.1 1.36-.2.23-.4.26-.75.09-.35-.18-1.47-.54-2.8-1.73-1.03-.92-1.73-2.05-1.93-2.4-.2-.35-.02-.54.15-.72.16-.16.35-.41.53-.61.18-.21.23-.35.35-.58.12-.23.06-.44-.03-.61-.09-.18-.78-1.9-1.07-2.6-.28-.68-.57-.59-.78-.6h-.66c-.23 0-.61.09-.93.44-.32.35-1.22 1.19-1.22 2.9s1.25 3.36 1.42 3.59c.18.23 2.45 3.74 5.93 5.25.83.36 1.48.57 1.99.73.84.27 1.6.23 2.2.14.67-.1 2.07-.84 2.36-1.65.29-.81.29-1.5.2-1.65-.09-.15-.32-.23-.67-.41Z"/>
</svg>"""
WA_ICON_DATA = "data:image/svg+xml;base64," + base64.b64encode(WA_ICON_SVG.encode("utf-8")).decode("ascii")

st.html(
    f"""
    <a
        href="{WHATSAPP_URL}"
        target="_blank"
        rel="noopener noreferrer"
        class="wa-floating"
        title="WhatsApp"
        aria-label="WhatsApp"
    >
        <img
            src="{WA_ICON_DATA}"
            class="wa-icon"
            alt="WhatsApp"
        >
    </a>
    """
)
