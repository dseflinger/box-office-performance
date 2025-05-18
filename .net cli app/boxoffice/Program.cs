using Npgsql;
using Dapper;
using System.Linq;
using ConsoleTables;

// todo do i need to hide my connection string?
var connectionString = "Host=localhost;Username=postgres;Password=danPost4247?;Database=boxoffice_db";

await using var dataSource = NpgsqlDataSource.Create(connectionString);
await using var connection = await dataSource.OpenConnectionAsync(); // might be able to skip this by connnecting to string directly

bool validDate = false;
DateTime date = new DateTime();

while (!validDate)
{
    Console.WriteLine("Enter a date: ");
    var dateString = Console.ReadLine();

    validDate = DateTime.TryParse(dateString, out date);
}

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
        1, 2";
// todo maybe add limit

var salesByTheater = connection.Query<SaleByTheater>(query, new { date = date }).ToList();
var topTheaterByRevenue = salesByTheater.OrderByDescending(x => x.TotalSum).FirstOrDefault();
var topTheaterByTickets = salesByTheater.OrderByDescending(x => x.TotalTickets).FirstOrDefault();

if (salesByTheater.Any() == true)
{
    Console.WriteLine("\n------------------------------Results Summary------------------------------\n");
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
    Console.WriteLine("No sales this day");
}

// maybe add keyboard things to leave if not built in?