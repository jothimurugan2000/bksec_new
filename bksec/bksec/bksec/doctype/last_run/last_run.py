from frappe.model.document import Document
import frappe

class LastRun(Document):
    pass

@frappe.whitelist()
def last_run():
    # Execute SQL query
    sql = """
        SELECT
            SUBSTRING_INDEX(job_attribute_1, '~', -1) AS `Total Records`,
            SUBSTRING_INDEX(SUBSTRING_INDEX(job_attribute_1, '~', 1),'~',-1 )AS `From Date`,
          SUBSTRING_INDEX(SUBSTRING_INDEX(job_attribute_1, '~', 2),'~',-1 )AS `To Date`,
          last_run_time as `Last Run time`
            
        FROM
            `tabLast Run` where job_type="{type}"
    """.format(type="IBEATS_LAST_MONTH_FETCH")
    results = frappe.db.sql(sql, as_dict=True)
    
    return results

@frappe.whitelist()
def last_run_mtd():
    # Execute SQL query
    sql = """
        SELECT
            SUBSTRING_INDEX(job_attribute_1, '~', -1) AS `Total Records`,
            SUBSTRING_INDEX(SUBSTRING_INDEX(job_attribute_1, '~', 1),'~',-1 )AS `From Date`,
          SUBSTRING_INDEX(SUBSTRING_INDEX(job_attribute_1, '~', 2),'~',-1 )AS `To Date`,
          last_run_time as `Last Run time`

        FROM
            `tabLast Run` where job_type="{type}"
    """.format(type="IBEATS_MTD_FETCH")
    results = frappe.db.sql(sql, as_dict=True)

    return results

# Return results
        # if results:
        #     return results[0].get('Job_Type'), results[0].get('Last_Run_time'), results[0].get('Total_Records')
        # else:
        #     frappe.throw(("No data found."))
