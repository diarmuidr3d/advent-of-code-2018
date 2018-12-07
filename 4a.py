input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

lines = input.split('\n')

def input_as_dict(input):
    logs = {}
    for line in lines:
        separated = line.split(']', 1)
        date = separated[0].replace('[', '')
        message = separated[1].strip()
        logs[date] = message
    return(logs)

def get_max_minute(minutes_list):
    i = 0
    max = 0
    ret = None
    while i < len(minutes_list):
        if minutes_list[i] > max:
            ret = i
            max = minutes_list[i]
        i = i +1
    return(ret)

logs = input_as_dict(input)
guard_times_asleep = {} # structured like so: {Guard: {total: 123, minutes: [0..59]}}
current_guard = None
current_guard_fell_asleep = None
for key in sorted(logs.keys()):
    message = logs[key]
    hash_index = message.find('#')
    if hash_index != -1:
        message_without_guard = message[hash_index + 1:]
        current_guard = message_without_guard[:message_without_guard.find(' ')].strip()
        if current_guard_fell_asleep:
            print("GUARD NEVER WOKE UP")
    elif message == "falls asleep":
        current_guard_fell_asleep = int(key.split(':')[1])
    elif message == "wakes up":
        current_guard_woke_up = int(key.split(':')[1])
        mins_asleep = current_guard_woke_up - current_guard_fell_asleep
        if current_guard not in guard_times_asleep:
            guard_times_asleep[current_guard] = {"total": mins_asleep, "minutes": [0]*60}
        else:
            guard_times_asleep[current_guard]["total"] = guard_times_asleep[current_guard]["total"] + mins_asleep
        min = current_guard_fell_asleep
        while min < current_guard_woke_up:
            guard_times_asleep[current_guard]["minutes"][min] = guard_times_asleep[current_guard]["minutes"][min] + 1
            min = min + 1
        current_guard_fell_asleep = None
    else:
        print("OH NOOOOOOOOO")

guard_max_mins_asleep = None
current_max_mins = 0
min_of_max_sleep = None
for guard in guard_times_asleep.keys():
    if guard_times_asleep[guard]["total"] > current_max_mins:
        guard_max_mins_asleep = guard
        current_max_mins = guard_times_asleep[guard]["total"]
        minutes = guard_times_asleep[guard]["minutes"]
        min_of_max_sleep = get_max_minute(minutes)
print(guard_max_mins_asleep)
print(current_max_mins)
print(min_of_max_sleep)
print("result", int(guard_max_mins_asleep) * int(min_of_max_sleep))
