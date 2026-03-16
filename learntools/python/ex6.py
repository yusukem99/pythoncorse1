import itertools

from learntools.core import *

import learntools.python.solns.word_search as word_search_module
word_search = word_search_module.word_search
import learntools.python.solns.multi_word_search as mws_module
multi_word_search = mws_module.multi_word_search
import learntools.python.solns.diamond as d_module
diamond = d_module.diamond
import learntools.python.solns.roulette_analysis as rou_module
roulette_gt = rou_module.conditional_roulette_probs

class ZA(EqualityCheckProblem):
    _var = 'length'
    _default_values = [-1]
    _expected = 0
    _solution = ("空文字列の長さは0です。なお、空文字列はブール値に変換したときに"
            "PythonがFalseとみなす唯一の文字列でもあります。")
class ZB(EqualityCheckProblem):
    _var = 'length'
    _default_values = [-1]
    _expected = 7
    _solution = ("Pythonは文字列の長さを数えるとき、スペース（や句読点）も含めることを"
            "覚えておきましょう。")
class ZC(EqualityCheckProblem):
    _var = 'length'
    _default_values = [-1]
    _expected = 7
    _solution = ("作成時に異なる構文を使っていますが、文字列 `c` は `b` と同じ内容です。"
            "特に、バックスラッシュは文字列の一部ではないため、長さには含まれない"
            "ことに注意してください。")
class ZD(EqualityCheckProblem):
    _var = 'length'
    _default_values = [-1]
    _expected = 3
    _solution = ("この文字列がトリプルクォート構文で作成されたことは、内容や長さには"
            "影響しません。この文字列は `'hey'` とまったく同じです。")
class ZE(EqualityCheckProblem):
    _var = 'length'
    _default_values = [-1]
    _expected = 1
    _solution = ("改行文字はたった1文字です！（Pythonでは2文字の組み合わせで"
            "表現しますが。）")

LightningLen = MultipartProblem(
        ZA,ZB,ZC,ZD,ZE,
        )

class ZipValidator(FunctionProblem):
    _var = 'is_valid_zip'

    _hint = ("`help(str.isdigit)` を調べてみましょう。")

    _solution = CS(
"""def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()""")

    _test_cases = [
            ('12345', True),
            ('1234x', False),
            ('1234', False),
            ('00000', True),
            ('', False),
            ('?', False),
    ]

class WordSearch(FunctionProblem):
    _var = 'word_search'

    _solution = CS.load(word_search_module.__file__)

    _hint = ("ここで役立つかもしれないメソッド: `str.split()`、`str.strip()`、"
            "`str.lower()`。"
            )

    _test_docs_a = [
            "The Learn Python Challenge Casino",
            "They bought a car, and a horse",
            "Casinoville?",
    ]
    _test_docs_b = _test_docs_a + ["He bought a casino. That's crazy."]
    _test_docs_c = [
            "The Learn Python Challenge Casino has a big casino full of casino games",
            "They bought a car",
            "Casinoville",
    ]

    _test_inputs = [
            (_test_docs_a, 'casino'),
            (_test_docs_a, 'ear'),
            (_test_docs_a, 'car'),
            (_test_docs_b, 'crazy'),
            (_test_docs_b, 'bought'),
            # Test for not double-counting repeated instances within a document
            (_test_docs_c, 'casino'),
            ([], 'spam'),
    ]
    _test_cases = [
            (args, word_search(*args))
            for args in _test_inputs
    ]


class MultiWordSearch(FunctionProblem):
    _var = 'multi_word_search'
    _solution = CS.load(mws_module.__file__)

    _test_docs_a = [
            "The Learn Python Challenge Casino",
            "They bought a car",
            "Casinoville?",
    ]
    _test_docs_b = _test_docs_a + ["He bought a casino. A casino! That's crazy."]
    _test_keywords = [
            [],
            ['casino'],
            ['casino', 'ear'],
            ['casino', 'ear', 'bought'],
    ]

    _test_cases = [
            (args, multi_word_search(*args))
            for args in itertools.product(
                [_test_docs_a, _test_docs_b, []],
                _test_keywords,
                )
            ]


class DiamondArt(FunctionProblem):
    _bonus = True
    _var = 'diamond'

    _solution = CS.load(d_module.__file__)

    _hint = ("`str` には文字列を特定の長さにパディングするためのメソッドがいくつかあります。"
            "ここで役立ちそうなのは `str.rjust()` や `str.center()` です。"
            )

    _test_heights = [2, 4, 0, 6]
    _test_cases = [
            (h, diamond(h))
            for h in _test_heights
            ]

    def check(self, fn):
        for args, expected in self._test_cases:
            orig_args = args
            # Wrap in tuple if necessary
            if not isinstance(args, tuple):
                args = args,
            try:
                actual = fn(*args)
            except Exception as e:
                actual = e

            assert actual is not None, ("height = {} のとき、戻り値が `None` でした。"
                    "return文を書き忘れていませんか？").format(args[0])
            orig_actual = actual
            # Ignore spaces to the right of the diamond itself for purposes
            # of comparison.
            # Also, okay, fine, allow final newline in their answer. I guess.
            if len(actual) > 0 and actual[-1] == '\n':
                actual = actual[:-1]
            normalize = lambda di: '\n'.join(line.rstrip() for line in di.split('\n'))
            anorm = normalize(actual)
            enorm = normalize(expected)
            actual_shown = (
                    repr(orig_actual) if (orig_actual + ' ').isspace()
                    else actual
                    )
            assert anorm == enorm, (
                    "このようなダイヤモンドが期待されましたが...\n\n"
                    "```\n{}\n```\n height={} のとき、実際にはこのようになりました...\n\n"
                    "```\n{}\n```\n").format(
                            expected,
                            args[0],
                            actual_shown,
                            )

class RouletteAnalyzer(FunctionProblem):
    _bonus = True
    _var = 'conditional_roulette_probs'

    _solution = CS.load(rou_module.__file__)

    _test_inputs = [
            [1, 3, 1, 5, 1],
            [1, 1, 1, 1,],
            [1, 2, 1],
            [5, 1, 3, 1, 2, 1 , 3, 3, 5, 1, 2],
            [1, 2, 1, 2, 1, 2, 1, 3],
    ]

    _test_cases = [
            (args, roulette_gt(args))
            for args in _test_inputs
            ]


qvars = bind_exercises(globals(), [
    LightningLen,
    ZipValidator,
    WordSearch,
    MultiWordSearch,
    DiamondArt,
    RouletteAnalyzer
    ],
    start=0,
)
__all__ = list(qvars)
