from app.ingestion import ingest_CSV

def test_ingest_CSV(valid_record,clean_expenses_table,connection):
    
    ingest_CSV([valid_record])
    cursor  = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    count = cursor.fetchone()[0]
    assert count == 1 
    cursor.close()


