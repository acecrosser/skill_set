using Calc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleCalcul
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Clear();
                string action;

                Console.WriteLine("Введите первое число:");
                var x = double.Parse(Console.ReadLine());
                
                Console.WriteLine("Введите второе число:");
                var y = double.Parse(Console.ReadLine());

                var result = CodeCalculator.Calc(x, y);

                action = Console.ReadLine();

                if (action == "+")
                {
                    Console.WriteLine("Решение:");
                    Console.WriteLine(result[0]);
                }
                else if (action == "-")
                {
                    Console.WriteLine("Решение:");
                    Console.WriteLine(result[1]);
                }
                else if (action == "*")
                {
                    Console.WriteLine("Решение:");
                    Console.WriteLine(result[2]);
                }
                else if (action == "/")
                {
                    if (y == 0)
                    {
                        Console.WriteLine("Деление на 0:");
                        Console.WriteLine(result[0]);
                    }
                    else
                    {
                        Console.WriteLine("Решение:");
                        Console.WriteLine(result[3]);
                    }
                }
                else
                {
                    Console.WriteLine("Ошибка, не корректная операция");
                }
                Console.ReadLine();
            }
        }
    }
}
