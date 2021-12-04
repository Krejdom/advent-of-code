using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day04
    {
        static void Main(string[] args)
        {
            string[] input = load_input();
            int[] drawn_nums = input[0].Split(',').Select(Int32.Parse).ToArray();
            List<BingoBoard> boards = load_boards(input);
            play(drawn_nums, boards);
        }
        private static string[] load_input()
        {
            //return System.IO.File.ReadAllLines(@"small-input.txt");
            return System.IO.File.ReadAllLines(@"input.txt");
        }
        private static List<BingoBoard> load_boards(string[] input)
        {
            List<BingoBoard> boards = new List<BingoBoard>();
            List<List<int>> board_lines = new List<List<int>>();
            BingoBoard new_board;
            for (int i = 2; i < input.Length; i++)
            {
                if (string.IsNullOrEmpty(input[i]))
                {
                    new_board = new BingoBoard(board_lines);
                    boards.Add(new_board);
                    board_lines = new List<List<int>>();
                }
                else
                {
                    string[] split_line1 = input[i].Trim().Replace("  ", " ").Split(' ');
                    List<int> split_line = split_line1.Select(Int32.Parse).ToList();
                    board_lines.Add(split_line);
                }
            }
            new_board = new BingoBoard(board_lines);
            boards.Add(new_board);
            return boards;
        }

        private static void play(int[] drawn_nums, List<BingoBoard> boards)
        {
            int playing_boards = boards.Count();
            foreach (int num in drawn_nums)
            {
                foreach (BingoBoard board in boards)
                {
                    if (!board.won)
                    {
                        board.mark(num);
                        if (board.won)
                        {
                            // part1
                            if (playing_boards == boards.Count())
                            {
                                Console.WriteLine(board.unmarked_nums_sum * num);
                            }
                            // part2
                            if (playing_boards == 1)
                            {
                                Console.WriteLine(board.unmarked_nums_sum * num);
                                return;
                            }
                            playing_boards -= 1;
                        }
                    }
                }
            }
        }
    }

    class BingoBoard
    {
        private List<List<int>> board_lines;
        public int unmarked_nums_sum;
        public bool won;
        public BingoBoard(List<List<int>> board_lines)
        {
            this.board_lines = board_lines;
            this.won = false;
            foreach (List<int> line in board_lines)
            {
                unmarked_nums_sum += line.Sum();
            }
        }

        public void mark(int num)
        {
            var (row, col) = find_num(num);
            if (row != -1)
            {
                unmarked_nums_sum -= num;
                board_lines[row][col] = -1;
            }
            update_win();
        }

        private (int, int) find_num(int num)
        {
            for (int row = 0; row < 5; row++)
            {
                for (int col = 0; col < 5; col++)
                {
                    if (board_lines[row][col] == num)
                    {
                        return (row, col);
                    }
                }
            }
            return (-1, -1);
        }

        private void update_win()
        {
            foreach (List<int> line in board_lines)
            {
                if (line.Sum() == -5)
                {
                    this.won = true;
                }
            }
            for (int col = 0; col < 5; col++)
            {
                int col_sum = 0;
                for (int row = 0; row < 5; row++)
                    col_sum += board_lines[row][col];
                if (col_sum == -5)
                {
                    this.won = true;
                }
            }
        }
    }
}
