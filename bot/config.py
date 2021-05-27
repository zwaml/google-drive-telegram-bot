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
        "**Google Drive Uploader**\n__I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
        
        f"**Authenticating Google Drive**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
        
        f"**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__\n\n**YouTube-DL Support**\n__Download files via youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
        
        f"**Delete Google Drive Files**\n__Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @haidarkrar**"
        ]
     
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **لقد تجاوزت الحد اليومي المسموح به .**\nحاول مرة اخرى بعد 24 ساعة .__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **الملف او المجلد المطلوب  **\_File id - {}  . غير موجود . تاكد بانه صحيح ومتاح بنفس الحساب المربوط بالبوت ."
    
    INVALID_GDRIVE_URL = "❗ **رابط قوقل درايف خاطئ **\nتاكد من ان الرابط بالصيغه الصحيحه ."
    
    COPIED_SUCCESSFULLY = "✅ **تم  النسخ بنجاح .**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **المعذرة لم تربطني باي حساب  حتى اقوم برفع الملفات .**\nارسل الامر  /{BotCommands.Authorize[0]} لربط  حساب قوقل درايف ."
    
    DOWNLOADED_SUCCESSFULLY = "📤 **جاري رفع الملف ...**\n**اسم الملف :** ```{}```\n**حجم الملف :** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **تم رفع الملف بنجاح .**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**فشل التحميل  **\n{}\n__الرابط  - {}__"
    
    DOWNLOADING = "📥 **جاري  تحميل الملف ...\nالرابط :** ```{}```"
    
    ALREADY_AUTH = "🔒 **البوت مربوط بالفعل بحساب  Google Drive .**\n استخدم الامر  /revoke لتسجيل الخروج من الحساب الحالي .\nأرسل لي رابطًا مباشرًا أو ملفًا للتحميل على Google Drive"
    
    FLOW_IS_NONE = f"❗ **الكود غير صحيح **\n اضغط  {BotCommands.Authorize[0]} اولا ."
    
    AUTH_SUCCESSFULLY = '🔐 **تم ربط حسابك بنجاح .**'
    
    INVALID_AUTH_CODE = '❗ **الكود غير صحيح **\nالرمز الذي أرسلته غير صالح أو تم استخدامه من قبل. قم بإنشاء واحد جديد من خلال عنوان URL الخاص بالمصادقة '
    
    AUTH_TEXT = "⛓️ **لربط البوت بحساب قوقل درايف الخاص بك   [اضغط هنا ]({}) ثم ارسل الكود الى هنا .**\nقم بالدخول للرابط بالاسفل  > اعطي البوت الصلاحيات  > سوف تحصل على كود  >انسخه  > ارسل الكود الى البوت "
    
    DOWNLOAD_TG_FILE = "📥 **جاري تحميل الملف...**\n**اسم الملف :** ```{}```\n**حجم الملف :** ```{}```\n**نوع الملف :** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **تم تعيين المجلد بنجاح .**\n ايدي المجلد الحالي هو  - {}\n استخدم  الامر  ```/{} clear``` لمسحه وتعيين المجلد الافتراضي '
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **تم استعادة الملف الافتراضي بنجاح .**\n يمكنك باي وقت استخدام الامر  ``` ( /{BotCommands.SetFolder[0]} رابط المجلد )``` لتعيين مجلد مجددا .'
    
    CURRENT_PARENT = "🆔 **اي المجلد الحالي هو  - {}**\nاستخدم  الامر  ```( /{} رابط المجلد )``` لتغييرة "
    
    REVOKED = f"🔓 **تم تسجيل الخروج من الحساب بنجاح .**\n بامكانك باي وقت استخدام الامر  /{BotCommands.Authorize[0]} لربط حسابك بالبوت مجددا ."
    
    NOT_FOLDER_LINK = "❗ **رابط  ملف غير صحيح .**\nالرابط الذي ارسلته عباره عن رابط مجلد ."
    
    CLONING = "🗂️ **جاري  الاستنساخ في قوقل درايف ...**\nالرابط    - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ أدخل عنوان URL صالحًا لـ Google Drive مع الأمر .**\nاستخدم  - ( /{} رابط قوقل درايف )__"
    
    INSUFFICIENT_PERMISSONS = "❗ **ليس لديك صلاحيات  كافية لهذا الملف.**\nرابط الملف  - {}"
    
    DELETED_SUCCESSFULLY = "🗑️✅ *تم حذف الملف بنجاح .**\nتم الحذف بشكل نهائي  !\nايدي الملف  - {}"
    
    WENT_WRONG = "⁉️ **خطأ: لقد حدث خطأ **\nالرجاء المحاولة لاحقا ."
    
    EMPTY_TRASH = "🗑️🚮**تم تفريغ سلة المهملات بنجاح  !**"
    
    PROVIDE_YTDL_LINK = "❗**الرجاء ارسال رابط يوتيوب .**"
