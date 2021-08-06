// Knight Tour problem
// taken from this youtube video https://www.youtube.com/watch?v=pwlxQeHchFQ
// https://www.educative.io/page/5641478634209280/5657382461898752
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Recursion
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] visited =   {{0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 },
                                {0,0,0,0,0,0,0,0 }};
            visited[0, 0] = 1;
            KnightTour(visited, 0, 0, 1);
            
            Console.ReadLine();
        }
        static int[] pathRow1 = { 2, 1, -1, -2, -2, -1, 1, 2 };

        static int[] pathCol1 = { 1, 2, 2, 1, -1, -2, -2, -1 };

        public static bool KnightTour(int[,] visited, int row, int col, int move)
        {
            if (move == 64)
            {
                for (int i = 0; i < 8; i++)
                {
                    for (int j = 0; j < 8; j++)
                    {
                        Console.Write($"{visited[i, j]}, ");
                    }
                    Console.WriteLine();
                }
                return true;
            }
            else
            {
                for (int index = 0; index < pathRow1.Length; index++)
                {
                    int rowNew = row + pathRow1[index];
                    int colNew = col + pathCol1[index];
                    if (IfValidMove(visited, rowNew, colNew))
                    {
                        move++;
                        visited[rowNew, colNew] = move;
                        if (KnightTour(visited, rowNew, colNew, move))
                        {
                            return true;
                        }
                        move--;
                        visited[rowNew, colNew] = 0;
                    }
                }
            }
            return false;
        }

        static bool IfValidMove(int[,] visited, int rowNew, int colNew)
        {
            if ((rowNew >= 0) && (rowNew < 8) && (colNew >= 0) && (colNew < 8) && (visited[rowNew, colNew] == 0))
            {
                return true;
            }
            return false;
        }
    }
}