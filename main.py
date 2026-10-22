"""ERP readiness coverage: missing, failed and orphaned acceptance scenarios."""
def coverage(requirements, scenarios):
    requirements = set(requirements)
    by_requirement = {key: [] for key in requirements}
    orphaned = []
    for row in scenarios:
        if row['status'] not in ('passed', 'failed', 'pending'):
            raise ValueError('Unknown test status')
        if row['requirement'] in by_requirement:
            by_requirement[row['requirement']].append(row['status'])
        else:
            orphaned.append(row['requirement'])
    return {'missing': sorted(key for key, states in by_requirement.items() if not states),
            'not_ready': sorted(key for key, states in by_requirement.items()
                                if states and any(state != 'passed' for state in states)),
            'orphaned': sorted(set(orphaned))}


if __name__ == '__main__':
    print(coverage(['PO-01','PO-02','PO-03'], [
        {'requirement':'PO-01','status':'passed'}, {'requirement':'PO-02','status':'failed'}]))
