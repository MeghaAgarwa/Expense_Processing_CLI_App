from app.analytics_runner import run_analytic_queries

def test_run_analytics(tmp_path):
    test_file = tmp_path/"test_querie.sql"
    test_file.write_text("SELECT COUNT(*) FROM expenses;")

    result = run_analytic_queries(str(test_file),interactive=False)
    assert result is None