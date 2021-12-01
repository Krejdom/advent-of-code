using System;

namespace AoC
{
    class Day01
    {
        static void Main(string[] args)
        {
            string[] file = LoadFile();
            int[] input = Array.ConvertAll(file, int.Parse);
            Console.WriteLine(Part1(input));
            Console.WriteLine(Part2(input));
        }

        static int Part1(int[] input)
        {
            int result = 0;
            for (int i=1; i < input.Length; i++)
            {
                int curDepth = input[i];
                int prevDepth = input[i-1];
                if (curDepth > prevDepth)
                {
                    result += 1;
                }
            }
            return result;
        }

        static int Part2(int[] input)
        {
            int result = 0;
            for (int i=3; i < input.Length; i++)
            {
                int curDepth = input[i] + input[i-1] + input[i-2];
                int prevDepth = input[i-1] + input[i-2] + input[i-3];
                if (curDepth > prevDepth)
                {
                    result += 1;
                }
            }
            return result;
        }

        static string[] LoadFile()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }
    }
}
