const dashboard_data = fetch('/api/getDashboardData/')
.then(response => response.json())
.then(data => {

    document.getElementById("total-machines").textContent = data.machines?.length;
    document.getElementById("repair-requests").textContent = data.repairRequests?.length
    document.getElementById("available-techs").textContent = data.technicians?.length
    data.working = data.machines.filter(f=>f.status == 'Working').length 
    data.not_working = data.machines.filter(mac=>mac.status == 'Need Repair').length
    const tableBody = document.getElementById("machine-table-body");
    data.machines.forEach(machine => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${machine.id}</td>
          <td>${machine.name}</td>
          <td>${machine.serial_number}</td>
          <td>${machine.status}</td>
          <td>${machine.importance}</td>
        `;
        tableBody.appendChild(row);
    });

    const labels = ['Working', 'Not Working'];
    const values = [
        data.working || 0,
        data.not_working || 0
    ];

    const ctx = document.getElementById('statusChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Machine Status',
                data: values,
                backgroundColor: ['rgba(44, 182, 9, 0.7)', 'rgba(243, 143, 29, 0.99)'],
                borderColor: ['rgba(5, 170, 27, 0.66)', 'rgb(250, 174, 12)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' },
                title: {
                    display: true,
                    text: 'Machines by Status'
                }
            }
        }
    });
});
