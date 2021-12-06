using System;
using System.Linq;

namespace AoC
{
    class Day06
    {
        static void Main(string[] args)
        {
            long[] input = load_input()[0].Split(',').Select(Int64.Parse).ToArray();
            FishSimulator fs = new FishSimulator(input);
            //fs.addDays(80);
            fs.addDays(256);
            Console.WriteLine(fs.fishTotal());
        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }
    }

    class FishSimulator
    {
        public long[] ages;
        public FishSimulator(long[] input)
        {
            this.ages = new long[9];
            foreach (long fish_age in input)
            {
                ages[fish_age] += 1;
            }
        }
        public void addDays(int days)
        {
            for (int i = days; i > 0; i--)
            {
                long[] tmp = new long[9];
                Array.Copy(ages, tmp, 9);
                ages[8] = tmp[0];
                ages[0] = tmp[1];
                ages[1] = tmp[2];
                ages[2] = tmp[3];
                ages[3] = tmp[4];
                ages[4] = tmp[5];
                ages[5] = tmp[6];
                ages[6] = tmp[7];
                ages[7] = tmp[8];

                ages[6] += tmp[0];
            }
        }
        public long fishTotal()
        {
            return ages.Sum();
        }
    }
}
