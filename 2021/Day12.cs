using System;
using System.Collections.Generic;

namespace AoC
{
    class Day12
    {
        static void Main(string[] args)
        {
            string[] input = load_input();
            Console.WriteLine(part1(input));
            Console.WriteLine(part2(input));
        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }
        private static Dictionary<string, HashSet<string>> GetCaveSystem(string[] input)
        {
            Dictionary<string, HashSet<string>> caves = new Dictionary<string, HashSet<string>>{};
            foreach (string path in input)
            {
                foreach (string name in path.Split('-'))
                {
                    if (!caves.ContainsKey(name))
                    {
                        caves[name] = new HashSet<string>{};
                    }
                }
                caves[path.Split('-')[0]].Add(path.Split('-')[1]);
                caves[path.Split('-')[1]].Add(path.Split('-')[0]);
            }
            return caves;
        }
        private static int part1(string[] input)
        {
            Dictionary<string, HashSet<string>> caves = GetCaveSystem(input);
            HashSet<string> possible_paths = new HashSet<string>{};
            FindAllPaths("start", new List<string>{}, caves, possible_paths);
            return possible_paths.Count;
        }
        private static void FindAllPaths(string start,
                                         List<string> interim_path,
                                         Dictionary<string, HashSet<string>> caves,
                                         HashSet<string> possible_paths)
        {
            interim_path.Add(start);
            if (start == "end")
            {
                possible_paths.Add(string.Join('-', interim_path));
                return;
            }
            foreach (string next_cave in caves[start])
            {
                if (!interim_path.Contains(next_cave) || char.IsUpper(next_cave[0]))
                {
                    FindAllPaths(next_cave, interim_path, caves, possible_paths);
                    interim_path.RemoveAt(interim_path.Count - 1);
                }
            }
        }
        private static int part2(string[] input)
        {
            Dictionary<string, HashSet<string>> caves = GetCaveSystem(input);
            HashSet<string> possible_paths = new HashSet<string>{};
            FindAllPaths2("start", new List<string>{}, caves, possible_paths, "");
            return possible_paths.Count;
        }
        private static void FindAllPaths2(string start,
                                          List<string> interim_path,
                                          Dictionary<string, HashSet<string>> caves,
                                          HashSet<string> possible_paths,
                                          string twice)
        {
            interim_path.Add(start);
            if (start == "end")
            {
                possible_paths.Add(string.Join('-', interim_path));
                return;
            }
            foreach (string next_cave in caves[start])
            {
                if (!interim_path.Contains(next_cave) || char.IsUpper(next_cave[0]))
                {
                    FindAllPaths2(next_cave, interim_path, caves, possible_paths, twice);
                    interim_path.RemoveAt(interim_path.Count - 1);
                }
                else if (twice == "" && next_cave != "start" && next_cave != "end")
                {
                    twice = next_cave;
                    FindAllPaths2(next_cave, interim_path, caves, possible_paths, twice);
                    interim_path.RemoveAt(interim_path.Count - 1);
                    twice = "";
                }
            }
        }
    }
}
