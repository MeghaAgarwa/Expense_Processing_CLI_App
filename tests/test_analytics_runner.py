from app.analytics_runner import run_analytic_queries

def test_run_analytics(connection,tmp_path):
    test_file = tmp_path/"test_querie.sql"
    test_file.write_text("SELECT COUNT(*) FROM expenses;")

    result = run_analytic_queries(str(test_file))
    assert result is None