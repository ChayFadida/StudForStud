import datetime
course_dict = {
    '11063': 'אנגלית בסיסי',
    '11064': 'אנגלית מתקדמים א',
    '11102': 'אלגברה 1 מח',
    '61740': 'מערכות ספרתיות',
    '61741': 'מבוא למדעי המחשב',
    '11006': 'חדו"א 2מ',
    '11060': 'אנגלית מתקדמים ב',
    '61738':'מבנים אלגבריים להנדסת תוכנה 1',
    '61743': 'מתמטיקה דיסקרטית 1',
    '61745': 'מבוא לתכנות מערכות',
    '61750': 'מבוא להנדסת תוכנה',
    '11129': 'טורים, התמרות ומשוואות דיפרנציאליות',
    '61739': 'מבני נתונים ומבוא לאלגוריתמים',
    '61774': 'יסודות המחשוב',
    '61778': 'לוגיקה להנדסת תוכנה',
    '61911': 'מבנים אלגבריים להנדסת תוכנה 2',
    '61912': 'ארכיטקטורת מערכות תוכנה',
    '61751': 'תכנות מונחה עצמים',
    '61752': 'מערכות הפעלה',
    '61753': 'אלגוריתמים',
    '61755': 'מערכות מסדי נתונים מ',
    '61762': 'ניהול פרויקטי תוכנה',
    '11069': 'אנגלית טכנית יישומית תוכנה',
    '61756': 'שיטות הנדסיות לפיתוח מערכות תוכנה',
    '61757': 'מבוא לבדיקות תוכנה',
    '61759': 'אוטומטים וחישוביות',
    '61760': 'הסתברות להנדסת תוכנה',
    '61769': 'ממשק אדם מחשב',
    '61179': 'מבוא לפיזיקה להנדסת תוכנה',
    '61180': 'פיזיקה להנדסת תוכנה ל',
    '61181': 'פיזיקה להנדסת תוכנה',
    '61761': 'כריית נתונים ומערכות לומדות',
    '61763': 'תורת הקומפילציה',
    '61775': 'מבוא לבינה מלאכותית',
    '61776': 'טכנולוגיות אינטרנט מתקדמות',
    '61765': 'רשתות מחשבים',
    '61767': 'אבטחת מידע וקריפטולוגיה',
    '61764': 'גרפיקה ממוחשבת',
    '61913': 'כלכלה חישובית ומסחר אלגוריתמי',
    '61956': 'חישוב מקבילי ומבוזר',
    '61959': 'אנליזה נומרית',
    '61960': 'מבוא לאופטימיזציה',
    '61961': 'אחזור מידע',
    '61962': 'גיאומטריה חישובית ומידול',
    '61964': 'ויזואליזציה של המידע',
    '61965': 'ניתוח של נתוני הרשתות',
    '61995': 'אלגוריתמים לטקסטים ורצפים',
    '61996': 'אלגוריתמים מבוזרים',
    '41942': 'מבוא לביולוגיה מולקולרית וגנטיקה להנדסת תוכנה',
    '61957': 'תורת המשחקים',
    '61958': 'תורת המידע',
    '61989': 'מחשבים קוונטים',
    '61991': 'תכנות מדעי',
    '61992': 'מבוא לחישה ולמידה',
    '61993': 'תורת המשחקים האלגוריתמית',
    '62002': 'עיבוד שפה טבעית עם למידת מכונה',
    '61971': 'עיבוד תמונה ספרתי',
    '61972': 'עיבוד אותות ספרתי DSP',
    '61973': 'תקשורת אלחוטית ורשתות מחשבים',
    '61974': 'בדיקת מערכות ספרתיות',
    '61975': 'דחיסת נתונים',
    '61976': 'ביולוגיה חישובית',
    '61994': 'למידה עמוקה עבור ראיית מכונה',
    '61834': 'מסדי נתונים מבוזרים',
    '61914': 'בלוקמין ומטבעות קריפטו',
    '61978': 'אימות תוכנה וחומרה',
    '61980': 'שפות תכנות',
    '61981': 'הנדסת דרישות',
    '61955': 'מחשוב זמן אמת',
    '62001': 'תכנות מקבילי',
    '62003': 'פרויקט במציאות רבודה',
    '62004': 'מבוא להנדסת מערכות ותעשיה 4.0',
    '11001': 'אלגברה',
    '11003': 'חדו"א 1',
    '11179': 'מבוא לפיזיקה אקדמית',
    '51104': 'מבוא להנדסת תעשייה',
    '61903': 'מבוא למדעי המחשב לתעו"נ',
    '11005': 'חדו"א 2',
    '11059': 'אנגלית מתקדמים ב',
    '11209': 'פיזיקה IE1',
    '21127': 'גרפיקה הנדסית לתעו"נ',
    '51005': 'מתמטיקה דיסקרטית',
    '51021': 'מבוא למדעי הנתונים',
    '51600': 'מבוא לכלכלה',
    '11210': 'פיזיקה IE2',
    '51431': 'מבוא למערכות ארגוניות',
    '51617': 'חשבונאות פיננסית',
    '51702': 'מודלים דטרמיניסטיים בחקב"צ',
    '51709': 'הסתברות',
    '51141': 'מערכות ייצור משולבות מחשב',
    '51215': 'תכן שיטות העבודה (חקר עבודה)',
    '51432': 'תכן וניהול של מערכות ארגוניות',
    '51703': 'מודלים סטוכסטיים בחקב"צ',
    '51723': 'סטטיסטיקה',
    '51131': 'ניהול מערכות ייצור',
    '51213': 'ניהול איכות סטטיסטי',
    '51429': 'אפיון וניתוח מערכות מידע',
    '51724': 'סימולציה ספרתית',
    '51022': 'חקר סיבתיות בביצועים',
    '51132': 'תכנון ותפעול תהליך האספקה בארגון',
    '51430': 'תכנון פרויקטים וניהולם',
    '51519': 'מסדי נתונים',
    '51955': 'חשבונאות ניהולית ומימון',
    '51136': 'תכן מערך העבודה',
    '21214': 'תהליכי עיבוד לתעו"נ',
    '51302': 'מבוא לשיווק',
    '51310': 'משוואות דיפרנציאליות ומערכות בקרה',
    '51013': 'תכן הנדסי',
    '51159': 'מעבדה במיב"מ (CIM)',
    '51138': 'הנדסת אנוש',
    '11002': 'אלגברה מ',
    '201154': 'סמינר בנושאים במתמטיקה',
    '201005': 'משוואות דיפרנציאליות רגילות מש',
    '201174': 'אלגברה לינארית 2',
    '51900': 'תורת ההסתברות מש',
    '201009': 'אנליזה נומרית מש',
    '201176': 'מבוא לאנליזה',
    '201178': 'מבוא לאופטימיזציה',
    '51901': 'תהליכים אקראיים מש',
    '201007': 'פונקציות מרוכבות מש',
    '201008': 'טורי פורייה והתמרות אינטגרליות מש',
    '201015': 'אלגברה מודרנית',
    '201006': 'משוואות דיפרנציאליות חלקיות מש',
    '201180': 'מערכות דינמיות מרוכבות',
    '201163': 'בניית מודלים מתמטיים',
    '31230': 'מבוא למחשבים',
    '31511': 'מיתוג ומערכות ספרתיות',
    '41090': 'כימיה א',
    '11121': 'משוואות דיפרנציאליות רגילות',
    '11231': 'פיזיקה 1מ',
    '31316': 'מבוא להנדסת חשמל',
    '31616': 'מבוא למדעי המחשב ושפת C',
    '11122': 'משוואות דיפרנציאליות חלקיות וטורי פורייה',
    '11123': 'פונקציות מרוכבות',
    '11232': 'פיזיקה 2מ',
    '31350': 'מוליכים למחצה',
    '51742': 'הסתברות ויסודות הסטטיסטיקה',
    '31401': 'תורת האלקטרוניקה התקבילית',
    '31402': 'מעבדת חשמל ואלקטרוניקה 1',
    '31421': 'אותות ומערכות',
    '31700': 'שדות ותמסורת גלים',
    '31891': 'מידול וסימולציה של מערכות דינאמיות',
    '31403': 'מעבדת חשמל ואלקטרוניקה 2',
    '31442': 'מבוא לעיבוד אותות ספרתי',
    '31521': 'אלקטרוניקה ספרתית',
    '31711': 'מבוא לתקשורת',
    '31910': 'מבוא לבקרה',
    '31999': 'המרת אנרגיה א',
    '11233': 'פיזיקה 3 מ',
    '31017': 'פרויקט תחרותי',
    '31451': 'אותות אקראיים ורעש מ',
    '31101': 'תכן הנדסי א',
    '31420': 'אותות ומערכות',
    '31430': 'רשתות ומערכות בדידות',
    '21218': 'חומרים ותהליכי עיבוד לתעו"נ',
    '31322': 'מבוא לחשמל',
    '51608': 'ניהול פיננסי',
    '51618': 'חשבונאות ניהולית',
    '41077': 'כימיה מכ',
    '22112': 'מבוא לגרפיקה הנדסית',
    '22705': 'מבוא יצירתי להנדסת מכונות',
    '22511': 'דינמיקה של חלקיקים',
    '22305': 'מכניקת מוצקים 1',
    '22400': 'הנדסת חומרים',
    '22106': 'מבוא לאלגוריתמיקה ותכנות',
    '22705': 'מבוא יצירתי להנדסת מכונות',
    '11133': 'משוואות דיפרנציאליות מכ',
    '11212': 'פיזיקה 2מכ',
    '22114': 'תיב"ם',
    '22310': 'מכניקת מוצקים 2',
    '22205': 'טכנולוגיה יישומית',
    '22415': 'מעבדה בחוזק וחומרים',
    '31375': 'חשמל ואלקטרוניקה מכ',
    '22600': 'תרמודינמיקה',
    '22512': 'דינמיקה של גוף קשיח',
    '22715': 'מבוא לתכן מכני',
    '22210': 'מבוא לתהליכי ייצור',
    '22800': 'אותות ומערכות',
    '22130': 'אנליזה נומרית',
    '22810': 'מבוא לבקרה',
    '22610': 'מכניקת זורמים',
    '22735': 'פרויקט תכן מכני',
    '22520': 'תורת הרטט',
    '22720': 'תכן רכיבים מכניים',
    '22861': 'מבוא למערכות מכטרוניות',
    '22467': 'מבוא לביומכניקה',
    '22993': 'תעשיה 4.0 – המפעל החכם',
    '22620': 'מעבר חום',
    '22635': 'מעבדה בתופעות מעבר',
    '22745': 'תכן הנדסי מתקדם',
    '11213': 'פיזיקה 3מכ',
    '51700': 'הסתברות וסטטיסטיקה מכ',
    '22251': 'תהליכי עיבוד שבבי',
    '22862': 'מעבדה במכטרוניקה',
    '22864': 'בקרה מודרנית',
    '22472': 'פולימרים בביומכניקה',
    '22855': 'גוף האדם כמערכת הנדסית',
    '22992': 'מבוא לרובוטים אוטונומיים',
    '22268': 'חוזק מתקדם',
    '22863': 'תכן מערכות משולבות',
    '22471': 'ניתוח הנדסי של מערכות פיזיולוגיות',
    '22994': 'תכן ותפעול שרשרת אספקה',
    '22853': 'יישומים מעשיים באלמנטים סופיים',
    '11004': 'חדוו״א 1מ',
    '51958': 'סטטיסטיקה למערכות מידע'
}

season_dict = {
    'קיץ': 'summer',
    'חורף': 'winter',
    'אביב': 'spring',
}
moded_dict ={
    'A': 'א',
    'B': 'ב',
    'C': 'ג',
    'Middle': 'אמצע'
}


def get_course_name(course_id):
    return course_dict.get(course_id, '')

def get_course_dict():
    return course_dict

def generate_years_array():
    current_year = datetime.datetime.now().year
    years_array = []
    for year in range(2009, current_year + 1):
        current_date = datetime.datetime.now().date()
        years_array.append(f"{year} חורף")
        years_array.append(f"{year} אביב")
        years_array.append(f"{year} קיץ")
    return years_array[::-1]  # Reverse the array
