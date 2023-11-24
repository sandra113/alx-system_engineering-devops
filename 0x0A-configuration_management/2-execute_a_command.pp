exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  notify      => Exec['start_killmenow_process'],
}

