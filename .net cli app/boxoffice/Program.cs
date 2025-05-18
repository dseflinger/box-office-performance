// See https://aka.ms/new-console-template for more information
using Npgsql;

// Console.WriteLine("Enter a date: ");
// var dateString = Console.ReadLine();

// if (DateTime.TryParse(dateString, out DateTime date))
// {
//     // todo handle logic
// }
// else
// {

//     Console.WriteLine("Please Enter a Valid Date");
// }

var connectionString = "Host=localhost;Username=postgres;Password=danPost4247?;Database=boxoffice_db";
await using var dataSource = NpgsqlDataSource.Create(connectionString);
await using var connection = await dataSource.OpenConnectionAsync(); // might be able to skip this by connnecting to string directly


await using var command = new NpgsqlCommand("SELECT name FROM boxoffice_movie ORDER BY id ASC", connection);
await using var reader = await command.ExecuteReaderAsync();

while (await reader.ReadAsync())
{
    Console.WriteLine(reader.GetString(0));
}

Console.WriteLine("didnt think it'd get this far did you???");


// todo create connection string and query db
// maybe add keyboard things to leave if not built in?