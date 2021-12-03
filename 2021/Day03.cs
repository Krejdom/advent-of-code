using System;
using System.Linq;
using System.Collections.Generic;

namespace AoC
{
    class Day03
    {
        static void Main(string[] args)
        {
            Submarine sub1 = new Submarine();
            Console.WriteLine(sub1.power_consumption);  // 198
            Console.WriteLine(sub1.ls_rating);          // 230
        }
    }

    class Submarine
    {
        private string[] diagnostic_report;
        private string gamma_rate;
        private string epsilon_rate;
        public int power_consumption;
        public int ls_rating;
        private string o_rating;
        private string co2_rating;

        public Submarine()
        {
            load_diagnostic_report();
            gamma_rate = calculate_gamma_rate(diagnostic_report);
            epsilon_rate = calculate_epsilon_rate();
            power_consumption = Convert.ToInt32(gamma_rate, 2) * Convert.ToInt32(epsilon_rate, 2);
            
            calculate_gass_rating(true);
            calculate_gass_rating(false);
            ls_rating = Convert.ToInt32(o_rating, 2) * Convert.ToInt32(co2_rating, 2);
        }
        private void load_diagnostic_report()
        {
            //diagnostic_report = System.IO.File.ReadAllLines(@"small-input.txt");
            diagnostic_report = System.IO.File.ReadAllLines(@"input.txt");
        }

        private string calculate_gamma_rate(string[] input)
        {
            string g_rate = "";
            int[] prevailing_bits = Enumerable.Repeat(0, input[0].Length).ToArray();
            foreach (string line in input)
            {
                for (int i = 0; i < line.Length; i++)
                {
                    if (line[i] == '0')
                    {
                        prevailing_bits[i] -= 1;
                    }
                    else
                    {
                        prevailing_bits[i] += 1;
                    }
                }
            }
            for (int i = 0; i < prevailing_bits.Length; i++)
            {
                if (prevailing_bits[i] >= 0)
                {
                    g_rate += "1";
                }
                else
                {
                    g_rate += "0";
                }
            }
            return g_rate;
        }

        private string calculate_epsilon_rate()
        {
            string e_rate = "";
            foreach (char ch in gamma_rate)
            {
                if (ch == '1')
                {
                    e_rate += "0";
                }
                else
                {
                    e_rate += "1";
                }
            }
            return e_rate;
        }

        private void calculate_gass_rating(bool is_o2)
        {
            int i = 0;
            List<string> candidates = diagnostic_report.ToList();
            string g_rate = gamma_rate;
            while (candidates.Count != 1)
            {
                List<string> new_candidates = new List<string>();
                foreach (string candidate in candidates)
                {
                    if ((is_o2 & (g_rate[i] == candidate[i])) |
                         !is_o2 & (g_rate[i] != candidate[i]))
                    {
                        new_candidates.Add(candidate);
                    }
                }
                i++;
                candidates = new_candidates;
                g_rate = calculate_gamma_rate(candidates.ToArray());
            }
            if (is_o2)
            {
                o_rating = candidates[0];
            }
            else
            {
                co2_rating = candidates[0];
            }
        }
    }
}
