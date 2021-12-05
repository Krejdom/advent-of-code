using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day05
    {
        static void Main(string[] args)
        {
            string[] input = load_input();
            List<Line> lines = parse_input(input);
            int[,] field = new int[1000, 1000];
            foreach (Line line in lines)
            {
                ////part1
                //if (line.is_horizontal | line.is_vertical)
                //{
                    foreach (Point p in line.all_points)
                    {
                        field[p.x, p.y] += 1;
                    }
                //}
                
            }
            Console.WriteLine(count_overlaps(field));
        }

        private static int count_overlaps(int[,] field)
        {
            int overlaps_total = 0;
            for (int i = 0; i < field.GetLength(0); i++)
            {
                for (int j = 0; j < field.GetLength(1); j++)
                {
                    if (field[i, j] > 1)
                    {
                        overlaps_total += 1;
                    }
                }
            }
            return overlaps_total;
        }

        private static void draw_fied(int[,] field)
        {
            for (int i = 0; i < field.GetLength(0); i++)
            {
                for (int j = 0; j < field.GetLength(1); j++)
                {
                    if (field[j, i] == 0){
                        Console.Write(".");
                    }
                    else
                    {
                        Console.Write(field[j, i]);
                    }
                    Console.Write(" ");
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }

        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }

        private static List<Line> parse_input(string[] input)
        {
            List<Line> lines = new List<Line>{};
            foreach (string line in input)
            {
                string[] points = line.Split(" -> ");

                int[] end1_coords = points[0].Split(',').Select(Int32.Parse).ToArray();
                int[] end2_coords = points[1].Split(',').Select(Int32.Parse).ToArray();
                Point end1 = new Point(end1_coords[0], end1_coords[1]);
                Point end2 = new Point(end2_coords[0], end2_coords[1]);

                lines.Add(new Line(end1, end2));
            }
            return lines;
        }
    }

    class Point
    {
        public int x;
        public int y;
        public Point(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }

    class Line
    {
        private Point end1;
        private Point end2;
        public bool is_horizontal = false;
        public bool is_vertical = false;
        public List<Point> all_points;
        public Line(Point end1, Point end2)
        {
            this.end1 = end1;
            this.end2 = end2;

            if (end1.y == end2.y)
            {
                this.is_horizontal = true;
            }
            else if (end1.x == end2.x)
            {
                this.is_vertical = true;
            }
            fill_all_points();
        }

        private void fill_all_points()
        {
            all_points = new List<Point>{};
            int x = end1.x;
            int y = end1.y;
            while (x != end2.x | y != end2.y)
            {
                all_points.Add(new Point(x, y));
                if (end2.x > end1.x)
                {
                    x += 1;
                }
                else if (end2.x < end1.x)
                {
                    x -= 1;
                }
                    
                if (end2.y > end1.y)
                {
                    y += 1;
                }
                else if (end2.y < end1.y)
                {
                    y -= 1;
                }
            }
            all_points.Add(new Point(x, y));
        }
    }
}
