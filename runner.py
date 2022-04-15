from hypy_utils import Timer

import pysenti

if __name__ == '__main__':
    timer = Timer()
    timer.log(pysenti.get_senti('I love you'))
    timer.log(pysenti.get_senti('I hate you'))

    timer.log(len(pysenti.get_senti_list(['I love cats'] * 10000)))
