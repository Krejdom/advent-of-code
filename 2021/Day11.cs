using System;

namespace AoC
{
    class Day11
    {
        static void Main(string[] args)
        {
            string[] input = load_input();
            int[,] energy_levels = new int[10, 10];
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    energy_levels[i, j] = input[i][j] - '0';
                }
            }
            Console.WriteLine(part1(energy_levels));
            Console.WriteLine(part2(energy_levels));
        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }

        private static bool will_flash(int[,] energy_levels)
        {
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    if (energy_levels[i, j] > 9)
                    {
                        return true;
                    }
                }
            }
            return false;
        }

        private static int[,] charge_neighbours(int[,] energy_levels, int i, int j)
        {
            if (i != 0)
            {
                if (energy_levels[i-1, j] != 0)
                {energy_levels[i-1, j] += 1;}
            }
            if (i != 9)
            {
                if (energy_levels[i+1, j] != 0)
                {energy_levels[i+1, j] += 1;}
            }
            if (j != 0)
            {
                if (energy_levels[i, j-1] != 0)
                {energy_levels[i, j-1] += 1;}
            }
            if (j != 9)
            {
                if (energy_levels[i, j+1] != 0)
                {energy_levels[i, j+1] += 1;}
            }
            if (i != 0 & j != 0)
            {
                if (energy_levels[i-1, j-1] != 0)
                {energy_levels[i-1, j-1] += 1;}
            }
            if (i != 0 & j != 9)
            {
                if (energy_levels[i-1, j+1] != 0)
                {energy_levels[i-1, j+1] += 1;}
            }
            if (i != 9 & j != 0)
            {
                if (energy_levels[i+1, j-1] != 0)
                {energy_levels[i+1, j-1] += 1;}
            }
            if (i != 9 & j != 9)
            {
                if (energy_levels[i+1, j+1] != 0)
                {energy_levels[i+1, j+1] += 1;}
            }

            return energy_levels;
        }

        private static int flash(int[,] energy_levels)
        {
            int total_flash = 0;
            for (int i = 0; i < 10; i++)
                {
                    for (int j = 0; j < 10; j++)
                    {
                        if (energy_levels[i, j] > 9)
                        {
                            total_flash += 1;
                            energy_levels[i, j] = 0;
                            energy_levels = charge_neighbours(energy_levels, i, j);
                        }
                    }
                }
            return total_flash;
        }

        private static void draw(int[,] energy_levels)
        {
            Console.WriteLine();
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    Console.Write(energy_levels[i, j]);
                }
                Console.WriteLine();
            }
        }

        private static int part1(int[,] energy_levels)
        {
            int total_flash = 0;
            for (int round = 0; round < 100; round++)
            {
                // add 1 to each
                for (int i = 0; i < 10; i++)
                {
                    for (int j = 0; j < 10; j++)
                    {
                        energy_levels[i, j] += 1;
                    }
                }
                // activate flashes
                while (will_flash(energy_levels))
                {
                    total_flash += flash(energy_levels);
                }
            }
            return total_flash;
        }

        private static bool not_synchronized(int[,] energy_levels)
        {
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    if (energy_levels[i, j] != 0)
                    {
                        return true;
                    }
                }
            }
            return false;
        }

        private static int part2(int[,] energy_levels)
        {
            int round = 0;
            while (not_synchronized(energy_levels))
            {
                round += 1;
                // add 1 to each
                for (int i = 0; i < 10; i++)
                {
                    for (int j = 0; j < 10; j++)
                    {
                        energy_levels[i, j] += 1;
                    }
                }
                // activate flashes
                while (will_flash(energy_levels))
                {
                    flash(energy_levels);
                }
            }
            return round + 100;
        }
    }
}
