using Npgsql;
using Dapper;
using System.Linq;
using ConsoleTables;

public class BoxOfficeApp
{
    private readonly string _connectionString;
    public BoxOfficeApp(string connectionString)
    {
        _connectionString = connectionString;
    }
    public async Task Run()
    {

        bool validDate = false;
        DateTime date = new DateTime();

        // todo maybe validation if future or way in the past dates
        while (!validDate)
        {
            Console.WriteLine("Enter a date: ");
            var dateString = Console.ReadLine();

            validDate = DateTime.TryParse(dateString, out date);
        }
        var sales = await GetSalesByTheater(date);
        DisplaySales(sales, date);
    }

    private async Task<List<SaleByTheater>> GetSalesByTheater(DateTime date)
    {
        await using var dataSource = NpgsqlDataSource.Create(_connectionString);
        await using var connection = await dataSource.OpenConnectionAsync(); // might be able to skip this by connnecting to string directly

        var query = @"
            SELECT 
                boxoffice_sale.theater_id AS theater, 
                boxoffice_theater.name AS name, 
                SUM(boxoffice_sale.amount) AS totalSum, 
                SUM(boxoffice_sale.tickets_sold) AS totalTickets, 
                ROUND((SUM(boxoffice_sale.amount) / SUM(boxoffice_sale.tickets_sold)), 2) AS costPerTicket 
            FROM 
                boxoffice_sale
            INNER JOIN 
                boxoffice_theater 
            ON 
                (boxoffice_sale.theater_id = boxoffice_theater.id) 
            WHERE 
                boxoffice_sale.date = @date 
            GROUP BY 
                1, 2
            LIMIT 50";

        var salesByTheater = connection.Query<SaleByTheater>(query, new { date = date }).ToList();
        return salesByTheater;
    }

    private void DisplaySales(List<SaleByTheater> salesByTheater, DateTime date)
    {
        if (salesByTheater.Any() == true)
        {
            var topTheaterByRevenue = salesByTheater.OrderByDescending(x => x.TotalSum).FirstOrDefault();
            var topTheaterByTickets = salesByTheater.OrderByDescending(x => x.TotalTickets).FirstOrDefault();

            Console.WriteLine("\n------------------------------Results Summary------------------------------\n");
            Console.WriteLine($"{date:MMMM dd, yyyy}");

            Console.WriteLine($"Top theater By Revenue:  {topTheaterByRevenue?.Name}");
            Console.WriteLine($"Top theater By Tickets:  {topTheaterByTickets?.Name}\n");
            Console.WriteLine("Sales by Theater");

            var table = new ConsoleTable("Name", "Total Revenue", "Total Tickets", "Cost Per Ticket");
            salesByTheater.ForEach(s => table.AddRow(s.Name, $"{s.TotalSum:C}", s.TotalTickets, $"{s.CostPerTicket:C}"));
            table.Write();
            Console.WriteLine();
        }
        else
        {
            Console.WriteLine($"\nNo sales for {date:MMMM dd, yyyy}");
        }
    }
}