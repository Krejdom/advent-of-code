using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day07
    {
        static void Main(string[] args)
        {
            List<int> input = load_input()[0].Split(',').Select(Int32.Parse).ToList();
            int min_position = input.Min();
            int max_position = input.Max();
            Console.WriteLine(part1(input, min_position, max_position));
            Console.WriteLine(part2(input, min_position, max_position));

        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }

        private static int part1(List<int> positioins, int min_p, int max_p)
        {
            int least_fuel = -1;
            for (int position = min_p; position <= max_p; position++)
            {
                int fuel = 0;
                foreach (int crab in positioins)
                {
                    fuel += Math.Max(crab, position) - Math.Min(crab, position);
                }
                if (fuel < least_fuel | least_fuel == -1){
                    least_fuel = fuel;
                }
            }
            return least_fuel;
        }
        private static int part2(List<int> positioins, int min_p, int max_p)
        {
            int least_fuel = -1;
            for (int position = min_p; position <= max_p; position++)
            {
                int fuel = 0;
                foreach (int crab in positioins)
                {
                    int difference = Math.Max(crab, position) - Math.Min(crab, position);
                    // https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
                    fuel += difference*(difference + 1) / 2;
                }
                if (fuel < least_fuel | least_fuel == -1){
                    least_fuel = fuel;
                }
            }
            return least_fuel;
        }
    }
}
