using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day10
    {
        static void Main(string[] args)
        {
            Dictionary<char, char> brackets = new Dictionary<char, char>();
            brackets.Add('(', ')');
            brackets.Add('[', ']');
            brackets.Add('{', '}');
            brackets.Add('<', '>');

            string[] input = load_input();
            Console.WriteLine(part1(input, brackets));
            Console.WriteLine(part2(input, brackets));

        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }

        private static int part1(string[] input, Dictionary<char, char> brackets)
        {
            int syntax_score = 0;
            foreach (string line in input)
            {
                syntax_score += corrupted_score(line, brackets);
            }
            return syntax_score;
        }

        private static long part2(string[] input, Dictionary<char, char> brackets)
        {
            List<long> scores = new List<long>{};
            foreach (string line in input)
            {
                if (corrupted_score(line, brackets) == 0)
                {
                    scores.Add(incomplete_score(line, brackets));
                }
            }
            scores.Sort();
            return scores[scores.Count / 2];
        }

        private static int get_closing_points(char b)
        {
            Dictionary<char, int> points = new Dictionary<char, int>();
            points.Add(')', 3);
            points.Add(']', 57);
            points.Add('}', 1197);
            points.Add('>', 25137);
            return points[b];
        }

        private static int get_opening_points(char b)
        {
            Dictionary<char, int> points = new Dictionary<char, int>();
            points.Add('(', 1);
            points.Add('[', 2);
            points.Add('{', 3);
            points.Add('<', 4);
            return points[b];
        }

        private static int corrupted_score(string line, Dictionary<char, char> brackets)
        {
            Stack<char> b_stack = new Stack<char>();
            foreach (char b in line)
            {
                if (brackets.ContainsKey(b))
                {
                    b_stack.Push(b);
                }
                else if (brackets.ContainsValue(b))
                {
                    char b0 = b_stack.Pop();
                    if (brackets[b0] != b)
                    {
                        return get_closing_points(b);
                    }
                }
            }
            return 0;
        }

        private static long incomplete_score(string line, Dictionary<char, char> brackets)
        {
            Stack<char> b_stack = new Stack<char>();
            foreach (char b in line)
            {
                if (brackets.ContainsKey(b))
                {
                    b_stack.Push(b);
                }

                else if (brackets.ContainsValue(b))
                {
                    b_stack.Pop();
                }
            }
            long score = 0;
            while (b_stack.Count != 0)
            {
                char ch = b_stack.Pop();
                score *= 5;
                score += get_opening_points(ch);
            }
            return score;
        }
    }
}
