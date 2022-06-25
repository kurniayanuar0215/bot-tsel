from cmath import exp
from email.policy import strict
import os
import logging
import glob
from datetime import datetime, timedelta
from tkinter.messagebox import YES
from turtle import left
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)
from multiprocessing import Process

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    user = update.message.from_user
    update.message.reply_text('Halo '+user['first_name']+' Welcome to PDC BOT'+'\n\n' +

                              '/prod <siteid> : Check lastest Productivity'+'\n' +
                              '/proddaily <start date> <finish date> <siteid> : Get Productivity'+'\n' +
                              '/prodkpi <start date> <finish date> <siteid> : Get Productivity from KPI Table'+'\n' +
                              '/prodns <start date> <finish date> : Get Productivity per NS'+'\n' +
                              '/dataplan <yearmonth> : Update Jabar dataplan'+'\n' +
                              '/user4g <start date> <finish date> <siteid> : Get KPI User 4G'+'\n' +
                              '/kpi <start date> <finish date> <siteid> : Get KPI file'+'\n' +
                              '/pychart : Get Trend Payload'+'\n' +
                              '/checktutela : Check last Tutela in FTP area & DB SQA'+'\n' +
                              '/resumetutela : Get Tutela Resume for Report'+'\n' +

                              '\n'+'date format = yyyy-mm-dd' +
                              '\n'+'yearmonth format = yyyymm')


def prod(update, context):
    user = update.message.from_user
    update.message.reply_text('Checking lastest Productivity, please wait...')
    str = update.message.text
    param = str.split(' ')
    exec(open("F:/KY/check_prod/prod_v3.py").read())
    update.message.bot.send_photo(
        update.message.chat.id, open('F:/KY/check_prod/out.jpg', 'rb'))
    # update.message.reply_text('/proddaily : Table Productivity Daily'+'\n' +
    #                           '/prodkpi : Table KPI Daily'+'\n')


def proddaily(update, context):
    update.message.reply_text('Get Productivity, please wait...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_daily_v2.py").read())
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_daily_v2.py").read())
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
        exec(open("F:/KY/prod/get_prod_daily_v2.py").read())
    else:
        update.message.reply_text('Format salah')

    filelist = glob.glob(os.path.join('F:/KY/prod/download/', "*"))
    for f in filelist:
        os.remove(f)


def prodkpi(update, context):
    update.message.reply_text(
        'Get Productivity from KPI table, please wait...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = ''
        exec(open("F:/KY/prodkpi/get_prod_daily_kpi.py").read())
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = ''
        exec(open("F:/KY/prodkpi/get_prod_daily_kpi.py").read())
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
        exec(open("F:/KY/prodkpi/get_prod_daily_kpi.py").read())
    else:
        update.message.reply_text('Format salah')

    filelist = glob.glob(os.path.join('F:/KY/prodkpi/download/', "*"))
    for f in filelist:
        os.remove(f)


def prodhourly(update, context):
    update.message.reply_text(
        'Get Productivity Hourly, please wait 5-10 minutes...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_hourly.py").read())
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_hourly.py").read())
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
        exec(open("F:/KY/prod/get_prod_hourly.py").read())
    else:
        update.message.reply_text('Format salah')

    filelist = glob.glob(os.path.join('F:/KY/prod/download/', "*"))
    for f in filelist:
        os.remove(f)


def prodkpihourly(update, context):
    update.message.reply_text(
        'Get Productivity Hourly from DB KPI, please wait 5-10 minutes...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_kpi_hourly.py").read())
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = ''
        exec(open("F:/KY/prod/get_prod_kpi_hourly.py").read())
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
        exec(open("F:/KY/prod/get_prod_kpi_hourly.py").read())
    else:
        update.message.reply_text('Format salah')

    filelist = glob.glob(os.path.join('F:/KY/prod/download/', "*"))
    for f in filelist:
        os.remove(f)


def kpi(update, context):
    update.message.reply_text('Get KPI, please wait...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = '''AND LEFT(siteid,3) IN ('BDG', 'BDK', 'BDS', 'CMI', 'COD', 'BDB', 'IND', 'SUB', 'CRB', 'CMS', 'KNG', 'MJL', 'CJR', 'SMD', 'BJR', 'TSK', 'GRT', 'PAN', 'BDX')'''
        exec(open("F:/KY/kpi/get_kpi.py").read())
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = '''AND LEFT(siteid,3) IN ('BDG', 'BDK', 'BDS', 'CMI', 'COD', 'BDB', 'IND', 'SUB', 'CRB', 'CMS', 'KNG', 'MJL', 'CJR', 'SMD', 'BJR', 'TSK', 'GRT', 'PAN', 'BDX')'''
        exec(open("F:/KY/kpi/get_kpi.py").read())
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
        exec(open("F:/KY/kpi/get_kpi.py").read())
    else:
        update.message.reply_text('Format salah')

    filelist = glob.glob(os.path.join('F:/KY/kpi/download/', "*"))
    for f in filelist:
        os.remove(f)


def user4g(update, context):
    update.message.reply_text('Get User 4G, please wait...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
        query_siteid = '''AND LEFT(siteid,3) IN ('BDG', 'BDK', 'BDS', 'CMI', 'COD', 'BDB', 'IND', 'SUB', 'CRB', 'CMS', 'KNG', 'MJL', 'CJR', 'SMD', 'BJR', 'TSK', 'GRT', 'PAN', 'BDX')'''
    elif count_param == 3:
        date_1 = param[1]
        date_2 = param[2]
        query_siteid = '''AND LEFT(siteid,3) IN ('BDG', 'BDK', 'BDS', 'CMI', 'COD', 'BDB', 'IND', 'SUB', 'CRB', 'CMS', 'KNG', 'MJL', 'CJR', 'SMD', 'BJR', 'TSK', 'GRT', 'PAN', 'BDX')'''
    elif count_param == 4:
        date_1 = param[1]
        date_2 = param[2]
        siteids = param[3]
        list = siteids.split(',')
        listToStr = ', '.join(f'"{w}"' for w in list)
        query_siteid = "AND a.`siteid` in ("+listToStr+")"
    else:
        update.message.reply_text('Format salah')

    exec(open("F:/KY/prod/get_4guser_daily_v2.py").read())

    filelist = glob.glob(os.path.join('F:/KY/prod/download/', "*"))
    for f in filelist:
        os.remove(f)


def dataplan(update, context):
    user = update.message.from_user
    update.message.reply_text('Data Plan process update, please wait...')
    str = update.message.text
    param = str.split(' ')
    count_param = len(param)

    if count_param == 2:
        yearmonth = param[1]
        years = yearmonth[0:4]
        months = yearmonth[4:6]

    exec(open("F:/KY/dataplan/get_v2.py").read())


def pychart(update, context):
    user = update.message.from_user
    update.message.reply_text('Please wait...')
    exec(open("F:/KY/prod/chart.py").read())
    exec(open("F:\KY\plot\plot.py").read())


def prodns(update: Update, context: CallbackContext) -> None:
    str = update.message.text
    prodns.param = str.split(' ')
    count_param = len(prodns.param)

    if count_param == 1 or count_param == 3:

        keyboard = [
            [
                InlineKeyboardButton("All NS", callback_data='prodns1'),
            ],
            [
                InlineKeyboardButton("BANDUNG", callback_data='prodns2'),
                InlineKeyboardButton("CIREBON", callback_data='prodns3'),
            ],
            [
                InlineKeyboardButton("SOREANG", callback_data='prodns4'),
                InlineKeyboardButton("TASIKMALAYA", callback_data='prodns5'),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Pilih NS :', reply_markup=reply_markup)
    else:
        update.message.reply_text('Format salah')


def prodns_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    count_param = len(prodns.param)
    raw_ns = query.data

    if count_param == 1:
        today = datetime.today() - timedelta(days=1)
        date_1 = today.strftime("%Y-%m-%d")
        date_2 = today.strftime("%Y-%m-%d")
    elif count_param == 3:
        date_1 = prodns.param[1]
        date_2 = prodns.param[2]

    if raw_ns == 'prodns1':
        final_ns = ""
        x = ''
        query_ns = ""
    elif raw_ns == 'prodns2':
        final_ns = "BANDUNG"
        x = '_'
        query_ns = "AND `branch` = '"+final_ns+"'"
    elif raw_ns == 'prodns3':
        final_ns = "CIREBON"
        x = '_'
        query_ns = "AND `branch` = '"+final_ns+"'"
    elif raw_ns == 'prodns4':
        final_ns = "SOREANG"
        x = '_'
        query_ns = "AND `branch` = '"+final_ns+"'"
    elif raw_ns == 'prodns5':
        final_ns = "TASIKMALAYA"
        x = '_'
        query_ns = "AND `branch` = '"+final_ns+"'"

    query.edit_message_text(text=f"Please wait...")

    exec(open("F:/KY/prodns/get_data.py").read())

    filelist = glob.glob(os.path.join('F:/KY/prodns/download/', "*"))
    for f in filelist:
        os.remove(f)


def checktutela(update, context):
    user = update.message.from_user
    exec(open("F:/KY/tutela/get_list.py").read())


def updatetutela(update, context):
    user = update.message.from_user
    str = update.message.text
    param = str.split(' ')

    try:
        yearweek = param[1]
        years = yearweek[0:4]
        weeks = yearweek[4:6]

        update.message.reply_text(
            'Update Tutela to FTP and DB, please wait 5-10 minutes...')
        exec(open("F:/KY/tutela/get_file.py").read())
        exec(open("F:/KY/tutela/get_file_resume.py").read())
    except:
        update.message.reply_text('Format Salah')


def resumetutela(update, context):
    user = update.message.from_user
    str = update.message.text
    param = str.split(' ')

    update.message.reply_text(
        'Get Tutela Resume, please wait...')

    try:
        yearweek = param[1]
        years = yearweek[0:4]
        weeks = yearweek[4:6]
        update.message.bot.sendDocument(update.message.chat.id, open(
            'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/'+years+'/RESUME/TUTELA_BORDER_MERGER_MM_W'+weeks+'.csv', 'rb'))
    except:
        update.message.reply_text('Format Salah / File tidak ditemukan')


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        "1991240221:AAEjSgb1_IigklBwPHGlse9e8LO6xJKBvwI", use_context=True, request_kwargs={
            'proxy_url': 'https://10.59.66.1:8080'}
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("prod", prod))
    dp.add_handler(CommandHandler("proddaily", proddaily))
    dp.add_handler(CommandHandler("prodhourly", prodhourly))
    dp.add_handler(CommandHandler("prodkpi", prodkpi))
    dp.add_handler(CommandHandler("prodkpihourly", prodkpihourly))
    dp.add_handler(CommandHandler("dataplan", dataplan))
    dp.add_handler(CommandHandler("pychart", pychart))
    dp.add_handler(CommandHandler("user4g", user4g))
    dp.add_handler(CommandHandler("kpi", kpi))
    dp.add_handler(CommandHandler("checktutela", checktutela))
    dp.add_handler(CommandHandler("updatetutela", updatetutela))
    dp.add_handler(CommandHandler("resumetutela", resumetutela))
    dp.add_handler(CommandHandler("prodns", prodns))
    dp.add_handler(CallbackQueryHandler(prodns_answer, pattern='prodns*'))

    #dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
