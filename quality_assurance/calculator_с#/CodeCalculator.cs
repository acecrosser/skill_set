using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calc
{
    public class CodeCalculator
    {
        public static double[] Calc(double x, double y)
        {
            if (y == 0)
            {
                var zero = x * 0;
                return new[] { zero };
            }
            else
            {
                var plus = x + y;
                var minus = x - y;
                var umno = x * y;
                var delen = x / y;

                return new[] { plus, minus, umno, delen };
            }
        }
    }
}
