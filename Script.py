class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {}</b>

<b>Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ <a href="@MOVIE_MASALA_46">ᴍᴏᴠɪᴇ ᴍᴀsᴀʟᴀ</a> Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>"""
    HELP_TXT = """<b>𝖧ᴇʏ {} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴏᴅᴜʟᴇ 🚩</b>"""
    ABOUT_TXT = """<b>𓄼 му иαмє : <a href="https://t.me/DWL_Movies_Finder_bot">ʝαииιє</a></b>
<b>𓄼 ¢яєαтσя : <a href="https://t.me/ULTRON_M">Hᴜᴢᴀɪғ 🇮🇳 [ OғғLɪɴᴇ ]</a></b>
<b>𓄼 ℓαиgυαgє : ρутнσи</b>
<b>𓄼 ℓιвяαяу : ρуяσgяαм</b>
<b>𓄼 ѕєяνєя  : нєяσкυ</b></a></b>
<b>𓄼 ℓαиgυαgє : ρутнσи</b>
<b>𓄼 ∂αтα вαѕє : мσиgσ ∂в</b>
<b>𓄼 вυιℓ∂ ѕтαтυѕ : ν10.0 [ɞeṭa]</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message
<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    OWNER_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟</b>
    
<b>• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴅᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ</b>
<b>• Uꜱᴇʀ ɴᴀᴍᴇ : @ULTRON_M</b>
<b>ᴅᴏɴ'ᴛ ʙᴇ ᴀғʀᴀɪᴅ ᴏғ ʙᴇɪɴɢ ᴅɪғғᴇʀᴇɴᴛ, ʙᴇ ᴀғʀᴀɪᴅ ᴏғ ʙᴇɪɴɢ ᴛʜᴇ sᴀᴍᴇ ᴀs ᴇᴠᴇʀʏ ᴏɴᴇ ᴇʟsᴇ</b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Eva Maria Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    ENGLISHSPELL_TXT = "<i><b>ʜᴇʟʟᴏ ɪ ᴄᴏᴜʟᴅ ɴᴏᴛ ғɪɴᴅ ᴛʜᴇ ᴍᴏᴠɪᴇ ʏᴏᴜ ᴀsᴋᴇᴅ ғᴏʀ  🥴</b>\n\n<b>ɢᴏᴏɢʟᴇ,ʏᴀɴᴅᴇx ᴄʟɪᴄᴋ ᴏɴ ᴀɴʏ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ғɪɴᴅ ᴛʜᴇ <u>ᴄᴏʀʀᴇᴄᴛ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ </u> ᴀɴᴅ ᴇɴᴛᴇʀ ɪᴛ ʜᴇʀᴇ ʙᴜᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ᴡɪʟʟ ʙᴇ ᴀᴠᴀɪʟᴀʙʟᴇ 🙃\n\nɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ᴇᴠᴇɴ ᴀғᴛᴇʀ ᴇɴᴛᴇʀɪɴɢ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ...</b>@ᴀᴅᴍɪɴ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ <b>ɪɴғᴏʀᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ.. ᴡᴇ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ᴡɪᴛʜɪɴ 24 ʜᴏᴜʀs 😇</b></i>"
    MALAYALMSPELL_TXT = "<i><b>ഹലോ നിങ്ങൾ ആവശ്യപ്പെട്ട ഈ സിനിമ എനിക്ക് കണ്ടെത്താൻ കഴിഞ്ഞില്ല 🥴 ...\n\nGoogle, Yandex ഏതെങ്കിലും ഒരു ബട്ടണിൽ ക്ലിക്ക് ചെയ്ത് ശരിയായ സിനിമയുടെ പേര് കണ്ടെത്തി ഇവിടെ നൽകുക എന്നാലേ സിനിമ / സീരിയസ് കിട്ടുകയുള്ളു 🙂...\n\nശരിയായ പേര് നൽകിയിട്ടും നിങ്ങൾക്ക് സിനിമ ലഭിക്കുന്നില്ലെങ്കിൽ ...</b> <code>@admin query</code>  <b>ഈ ഫോർമാറ്റിൽ അഡ്മിനെ അറിയിക്കുക .. ഞങ്ങൾ 24 മണിക്കൂറിനുള്ളിൽ അപ്‌ലോഡ്  ചെയ്യും 😇</b></i>"
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Eva Maria
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📂 ᴛᴏᴛᴀʟ ғɪʟᴇs:</b> <code>{}</code>
<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs:</b> <code>{}</code>
<b>♻️ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs:</b> <code>{}</code>
<b>🗃️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ:</b> <code>{}</code> MiB
<b>🆓 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ:</b> <code>{}</code> MiB""" 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
