import texttable
import datetime
import pyperclip


def get_server_timestamp(datetime_string: str):
    return datetime.datetime.strptime(datetime_string, "%I:%M %p - %m/%d")


def get_table_header():
    return ["layer", "last kill time (server time)", "skinned at kill time", "min ETA (kill time + 6 hours)", "max ETA (kill time + 23 hours)"]


def format_row_data(layer: int, kill_time: datetime.datetime, skinned: str):
    return_list = []
    last_kill_string = kill_time.strftime("%I:%M %p - %m/%d")
    min_eta_time = kill_time + datetime.timedelta(0, 0, 0, 0, 0, 6, 0)
    max_eta_time = kill_time + datetime.timedelta(0, 0, 0, 0, 0, 23, 0)
    return_list.append(str(layer))
    return_list.append(last_kill_string)
    return_list.append(skinned)
    return_list.append(min_eta_time.strftime("%I:%M %p - %m/%d"))
    return_list.append(max_eta_time.strftime("%I:%M %p - %m/%d"))
    return return_list


def get_table(my_data: list[list]):
    table = texttable.Texttable()
    # table formatting
    table.set_cols_align(["c", "c", "c", "c", "c"]) # (l)eft, (r)ight, (c)enter
    table.set_cols_valign(["m", "m", "m", "m", "m"]) # (t)op, (m)iddle, (b)ottom
    # add rows here
    table.add_rows(my_data)
    return table.draw()


def get_output(table):
    return "Mankrik TLPD Spawn Timer Quick Reference Chart:\n\n" + \
    "```\n" + \
    f"{table}\n" + \
    "```\n" #+ \
    #If this message has a :white_check_mark: reaction by Giskard, it is currently accurate."


if __name__ == "__main__":
    layer1_ts = get_server_timestamp("04:51 am - 11/5")
    layer2_ts = get_server_timestamp("03:59 pm - 11/4")
    layer3_ts = get_server_timestamp("10:42 pm - 11/5")
    layer4_ts = get_server_timestamp("09:46 am - 11/5")
    layer5_ts = get_server_timestamp("05:17 pm - 11/5")

    table_data = [
        get_table_header(),
        format_row_data(1, layer1_ts, "NO"),
        format_row_data(2, layer2_ts, "NO - TLPD"),
        format_row_data(3, layer3_ts, "NO - TLPD"),
        format_row_data(4, layer4_ts, "NO"),
        format_row_data(5, layer5_ts, "NO"),
    ]

    table = get_table(table_data)
    output = get_output(table)

    print(output)
    pyperclip.copy(output)