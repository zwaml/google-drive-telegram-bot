class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**مرحبا عزيزي {}.**\n__أنا Google Drive Uploader Bot يمكنك استخدامه لتحميل أي ملف / فيديو إلى Google Drive من رابط مباشر أو ملفات Telegram.\nلمعرفة كيف استخدام البوت اضغط  /help."

   HELP_MSG = [
        ".",
        "**Google Drive Uploader**\nيمكنني تحميل الملفات من رابط مباشر أو ملفات Telegram إلى Google Drive الخاص بك. كل ما أحتاجه هو ربط البوت  على حساب Google Drive الخاص بك وإرسال رابط تنزيل مباشر أو ملف Telegram.\n\nلدي ايضا المزيد من المميزات ... !هل تريد ان تكتشف ذلك  ? فقط تابع الخطوات التوضيحية التالية بعناية .",
        
        f"**ربط البوت بحساب قوقل درايف **\nارسل  الامر  /{BotCommands.Authorize[0]} وسوف تحصل على رابط المصادقة , ادخل على الرابط بالزر بالاسفل واتبع كل الخطوات وقم بنسخ الكود الذي سوف تحصل عليه وارسله الى هنا . استخدم الامر  /{BotCommands.Revoke[0]}  لتسجيل الخروج من قوقل درايف باي وقت تريد ذلك.__\n\n**ملاحظة : انا لا افهم ولا استجيب لاي امر الا فقط   الامر ( /{BotCommands.Authorize[0]} ) حتى تقوم بربط البوت بحساب قوقل درايف  .\nلذلك ربط البوت بحساب قوقل درايف اجباري كي اعمل بشكل صحيح !**",
        
        f"**تحميل الروابط المباشرة **\n يمكنك ايضا ارسال رابط مباشر لاي ملف وانا ساقوم بتحميله للسيرفر الخاص بالبوت ثم ارفعه الى حسابك بقوقل درايف .تستطيع ايضا اعادة تسمية الملفات قبل رفعها لقوقل درايف  . فقط ارسل لي رابط التحميل المباشر ثم  علامة  ' | ' ثم الاسم الجديد للملف .__\n\n**مثال ذلك :**\n```https://example.com/AFileWithDirectDownloadLink.mkv | اسم-الملف.mkv```\n\n**ملفات تلقرام **\nلرفع  ملفات telegram الى  حساب Google Drive الخاص بك ، ما عليك سوى إرسال الملف إلي وسأقوم بتنزيله وتحميله إلى حساب Google Drive الخاص بك. ملاحظة : تنزيل ملفات Telegram بطيء. قد يستغرق الأمر وقتًا أطول للملفات الكبيرة.__\n\n**البوت ايضا يدعم تحميل فديوهات اليوتيوب**\nلتحميل فديوهات يوتيوب ورفعها الى قوقل درايف .\nاستخدم الامر  مثال ذلك :  /{BotCommands.Ytdl[0]} رابط اليوتيوب ",
        
        f"**تعيين مجلد معين **\nهل ترغب ان ترفع الملفات الى مجلد معين ا الى  **TeamDrive**  ?\n استخدم الامر ( /{BotCommands.SetFolder[0]} رابط المجلد ) لتخصيص مجلد معين .\nكل الملفات سوف ارفعها الى المجلد المعين الذي قمت بتخصيصه .",
        
        f"**حذف ملفات Google Drive **\n لحذف اي ملف او اي مجلد  بقوقل درايف . استخدم الامر ( /{BotCommands.Delete[0]} رابط المجلد / رابط الملف) .\nيمكنك ايضا تفريغ سلة المهملات  باستخدام  الامر  /{BotCommands.EmptyTrash[0]}\nملاحظة : الملفات ستحذف بشكل نهائي . هذه العملية لا يمكن الغاؤها .\n\n**نسخ ملفات  Google Drive **\nنعم استنساخ  ونسخ ,ملفات  Google Drive .\n لعمل ذلك استخدم الامر ( /{BotCommands.Clone[0]} ايدي الملف / ايدي المجلد او رابطه ) لاستنساخ اي ملف او مجلد على حسابك ",
        
        "**القواعد  & التحذيرات **\n 1.لا تنسخ ملفات / مجلدات Google Drive الكبيرة. قد يتعطل الروبوت وقد تتلف ملفاتك.\n2. أرسل طلبًا واحدًا في كل مرة  وانتظر حتى يكمل البوت العملية ما لم سيوقف البوت جميع العملياتs.\n3. لا ترسل للبوت روابط بطيئة التحميل .\n4. لا تسيء استخدام هذه الخدمة المجانية أو تفرط في تحميلها أو تسيء استخدامها فيما لا يرضي الله  وفي الاخير شكرا لكم لاستخدامكم البوت الخاص بنا  وتقبلوا خالص تحاياتي  أخوكم المجاهد عدي الغولي.",
        
        # Dont remove this ↓ if you respect developer.
        "**تم تطوير البوت بواسطة  @haidarkrar**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
