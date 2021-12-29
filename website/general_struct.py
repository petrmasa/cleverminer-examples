import pandas as pd
import sys

from cleverminer.cleverminer import cleverminer

#prepare panda dataset here

hypo = cleverminer(df=df, proc=<procedure>, 
          quantifiers = <quantifiers>,
          ante = <cedent>,
          succ = <cedent>,
          cond = <cedent>).result
cleverminer.print_hypolist(hypo)
