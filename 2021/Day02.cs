using System;

namespace AoC
{
    class Day02
    {
        static void Main(string[] args)
        {
            string[] file = LoadFile();
            Console.WriteLine(Part1(file));
            Console.WriteLine(Part2(file));
        }

        static int Part1(string[] input)
        {
            int depth = 0;
            int position = 0;
            foreach (string line in input)
            {
                string[] command = line.Split(" ");
                if (command[0] == "forward")
                {
                    position += Int32.Parse(command[1]);
                }
                else if (command[0] == "down")
                {
                    depth += Int32.Parse(command[1]);
                }
                else if (command[0] == "up")
                {
                    depth -= Int32.Parse(command[1]);
                }
            }
            return depth * position;
        }

        static int Part2(string[] input)
        {
            int depth = 0;
            int position = 0;
            int aim = 0;
            foreach (string line in input)
            {
                string[] command = line.Split(" ");
                if (command[0] == "forward")
                {
                    position += Int32.Parse(command[1]);
                    depth += aim * Int32.Parse(command[1]);
                }
                else if (command[0] == "down")
                {
                    aim += Int32.Parse(command[1]);
                }
                else if (command[0] == "up")
                {
                    aim -= Int32.Parse(command[1]);
                }
            }
            return depth * position;
        }

        static string[] LoadFile()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }
    }
}
